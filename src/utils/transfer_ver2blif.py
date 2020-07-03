import sys
import os

file_path = sys.argv[1]
f_read = open(file_path, 'r')
new_file_path = os.path.splitext(file_path)[0]+'.blif'
f_write = open(new_file_path, 'w+')

ios = ['input', 'output', 'wire', 'reg']
gates = ['buf', 'and', 'or', 'not', 'nand', 'nor', 'xor', '_DC', '_HMUX']
while True:
	line = f_read.readline()
	if line:
		temp = line.split(' ')
		if temp[0] == 'module':
			lines [line]
			while line.strip()[-2] != ';':

		if temp[0] in ios:
			temp.insert(1,'[1:0]')
			f_write.write(" ".join(temp))
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