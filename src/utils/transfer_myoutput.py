import sys
import os
from collections import defaultdict

file_path_gf = sys.argv[1]
f_gf = open(file_path_gf, 'r')
new_file_path = os.path.join(os.path.dirname(file_path_gf), 'my_output.blif')
const_file_path = os.path.join(os.path.dirname(file_path_gf), 'my_const.blif')
print(new_file_path)
f_write = open(new_file_path, 'w+')
f_const = open(const_file_path, 'w+')

f_write.write('.model top\n')
f_const.write('.model top\n')

input_names_gf = []
output_names_gf = []
while True:
	line = f_gf.readline()
	if line:
		temp = line[:-1].split(' ')
		key = temp[0]
		if key == '.inputs':
			input_names_gf = temp[1:]
			f_write.write('.inputs ')
			f_const.write('.inputs ')
			for i in range(len(input_names_gf)//2):
				f_write.write('input%d ' % i)
				f_const.write('input%d ' % i)
			f_write.write('\n')
			f_const.write('\n')
			#f_write.write(line)
			f_write.write('.outputs out\n')
			f_const.write('.outputs out\n')
		elif key == '.outputs':
			output_names_gf = temp[1:]
		else:
			continue
	else:
		f_gf.close()
		break

f_const.write('.names out\n0\n')
f_const.write('.end\n')
f_const.close()

subckt = ['.subckt']
for i in range(len(input_names_gf)//2):
	transformerinputs = ['A=input%d' % i]
	transformeroutputs = ["Y2=%s Y1=%s" % (input_names_gf[2*i], input_names_gf[2*i+1])]
	f_write.write(" ".join(subckt + ['inputtransformer'] + transformerinputs + transformeroutputs) + '\n')
inputs = [ i+'='+i for i in input_names_gf]
outputs_g = [ i+'='+i+'_g' for i in output_names_gf ]
outputs_r = [ i+'='+i+'_r' for i in output_names_gf ]
f_write.write(" ".join(subckt + ['gold'] + inputs + outputs_g) + '\n')
f_write.write(" ".join(subckt + ['gate'] + inputs + outputs_r) + '\n')
f_write.write('\n')

superor = ['.subckt', 'superor']
for i in range(len(output_names_gf)//2):
	superor.append('out'+str(i)+'='+'out'+str(i))
	temp = ".subckt miter B=%s A=%s D=%s C=%s Y=%s" % (output_names_gf[2*i]+'_g', output_names_gf[2*i+1]+'_g', output_names_gf[2*i]+'_r', output_names_gf[2*i+1]+'_r', 'out'+str(i))
	f_write.write(temp + '\n')
superor.append('out=out')
f_write.write(" ".join(superor) + '\n')
f_write.write('.end\n')
f_write.write('\n')

for i in range(3):
	file_path = sys.argv[i+1]
	f_read = open(file_path, 'r')
	lines = f_read.read() 
	f_write.write(lines + '\n')

f_write.write('.model superor\n')
inputs = " ".join(['.inputs'] + [ 'out'+str(i) for i in range(len(output_names_gf)//2)])
f_write.write(inputs + '\n')
f_write.write('.outputs out\n')
names = ['.names'] + [ 'out'+str(i) for i in range(len(output_names_gf)//2)] + ['out']
f_write.write(" ".join(names) + '\n')
temp = ['-'] * (len(output_names_gf)//2)
for i in range(len(output_names_gf)//2):
	temp[i] = '1'
	f_write.write("".join(temp) + ' 1\n')
	temp[i] = '-'
f_write.write('.end\n')

ors = defaultdict(set)

f_gf_or = open('Mgfor.txt', 'r')
while True:
	line = f_gf_or.readline()
	if line:
		temp = line.split(' ')
		ors[temp[0]].add(int(temp[1]))
	else:
		break
f_gf_or.close()

f_rf_or = open('Mrfor.txt', 'r')
while True:
	line = f_rf_or.readline()
	if line:
		temp = line.split(' ')
		ors[temp[0]].add(int(temp[1]))
	else:
		break
f_rf_or.close()

def loop(x, num, total, f):
	if num == total:
		if '1' in x:
			f.write(x + ' 1\n')
	else:
		op = ['00','1-']
		for i in op:
			loop(x+i, num+1, total, f)

for k in list(ors.keys()):
	for n in ors[k]:
		if k == 'mor':
			f_write.write('.model %s%s\n' % (k, str(n)))
			inputs = " ".join(['.inputs'] + [ chr(65 + i) for i in range(n)])
			f_write.write(inputs + '\n')
			f_write.write('.outputs Y1 Y2\n')

			names = ['.names'] + [ chr(65 + i) for i in range(n)] + ['Y1']
			f_write.write(" ".join(names) + '\n')
			loop('', 0, n//2, f_write)
			
			names = ['.names'] + [ chr(65 + i) for i in range(n)] + ['Y2']
			f_write.write(" ".join(names) + '\n')
			temp = ['-'] * n
			for i in range(0,n,2):
				temp[i] = '0'
				temp[i+1] = '1'
				f_write.write("".join(temp) + ' 1\n')
				temp[i] = '-'
				temp[i+1] = '-'
			f_write.write('.end\n')
			f_write.write('\n')
		elif k == 'mnor':
			f_write.write('.model %s%s\n' % (k, str(n)))
			inputs = " ".join(['.inputs'] + [ chr(65 + i) for i in range(n)])
			f_write.write(inputs + '\n')
			f_write.write('.outputs Y1 Y2\n')

			names = ['.names'] + [ chr(65 + i) for i in range(n)] + ['Y1']
			f_write.write(" ".join(names) + '\n')
			loop('', 0, n//2, f_write)
			names = ['.names'] + [ chr(65 + i) for i in range(n)] + ['Y2']
			f_write.write(" ".join(names) + '\n')
			temp = ['0'] * n
			f_write.write("".join(temp) + ' 1\n')
			f_write.write('.end\n')
			f_write.write('\n')

f_write.close()