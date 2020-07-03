import sys
import os

file_path = sys.argv[1]
print(file_path)
f_read = open(file_path, 'r')
new_file_path = os.path.join(os.path.dirname(file_path), 'M'+os.path.basename(file_path))
print(new_file_path)
f_write = open(new_file_path, 'w+')

ios = ['input', 'output', 'wire', 'reg']
gates = ['buf', 'and', 'or', 'not', 'nand', 'nor', 'xor', 'xnor', '_DC', '_HMUX']
while True:
	line = f_read.readline()
	if line:
		temp = line.split(' ')
		if temp[0] in ios:
			line = line[:-1]
			while line[-1] != ';':
				line = line + f_read.readline()[:-1]
			temp = line.split(' ')
			temp.insert(1,'[1:0]')
			f_write.write(" ".join(temp) + '\n')
		elif temp[0] in gates:
			temp = list(map(lambda x: x.strip(), line.split(';')))
			for i in temp:
				if i == '' or i == ' ' or i == '\n':
					continue
				temptemp = i.split(' ')
				if temptemp[0] in gates:
					f_write.write('m' + " ".join(temptemp) +';\n')
				else:
					f_write.write(i+'\n')
		else:
			f_write.write(line)
			
	else:
		break

f_read.close()
f_write.close()