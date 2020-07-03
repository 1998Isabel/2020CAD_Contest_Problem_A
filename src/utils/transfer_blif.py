import sys
import os

file_path = sys.argv[1]
print(file_path)
f_read = open(file_path, 'r')
new_file_path = os.path.join(os.path.dirname(file_path), 'new_'+os.path.basename(file_path))
print(new_file_path)
f_write = open(new_file_path, 'w+')
f_or_write = open(os.path.splitext(file_path)[0]+"or.txt", 'w+')

mors = set()
mnors = set()

while True:
	line = f_read.readline()
	if line:
		temp = line.split(' ')
		if temp[0] == '.subckt':
			# print(temp)
			temp[-1] = temp[-1].strip('\n')
			ios = temp[4:] + temp[2:4]
			for i in range(len(ios)):
				# print(ios)
				inside = ios[i].split('=')
				# print(inside)
				if i == len(ios) - 1 or i == len(ios) - 2:
					inside[0] = 'Y1' if i == len(ios) - 1 else 'Y2'
				else:
					inside[0] = chr(65 + (i//2)*2 + abs(1 - i%2))
				ios[i] = "=".join(inside)
				# print("AFTER:", ios[i])
			if temp[1] == 'mor':
				mors.add(len(ios)-2)
				temp[1] = 'mor'+str(len(ios)-2)
			elif temp[1] == 'mnor':
				mnors.add(len(ios)-2)
				temp[1] = 'mnor'+str(len(ios)-2)
			temp = temp[0:2] + ios
			# print(temp)
			f_write.write(" ".join(temp) + '\n')
		else:
			f_write.write(line)
			
	else:
		break
f_read.close()
f_write.close()

print(mors, mnors)

for n in mors:
	f_or_write.write('mor %s\n' % (str(n)))
for m in mnors:
	f_or_write.write('mnor %s\n' % (str(m)))

f_or_write.close()