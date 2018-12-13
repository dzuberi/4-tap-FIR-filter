in_file = open('adder.vec','r')
text_file = open('output.vec','w')

for i in range(0,13):
	text_file.write(in_file.readline())

for a in range(0,64):
	for b in range(0,64):
		f = a + b
		astr = '{0:06b}'.format(a)
		bstr = '{0:06b}'.format(b)
		fstr = '{0:06b}'.format(f)
		#print(len(fstr))
		if len(fstr) > 6:
			fstr = fstr[1:]
		#fstr = fstr[1:len(fstr)]
		a5_4 = int(astr[0:2],2)
		a3_0 = int(astr[2:],2)
		b5_4 = int(bstr[0:2],2)
		b3_0 = int(bstr[2:],2)
		f5_4 = int(fstr[0:2],2)
		f3_0 = int(fstr[2:],2)
		line = '{0:01x}'.format(a5_4) + ' ' + '{0:01x}'.format(a3_0) + ' ' + '{0:01x}'.format(b5_4) + ' ' + '{0:01x}'.format(b3_0)+ ' ' + '{0:01x}'.format(f5_4) + ' ' + '{0:01x}'.format(f3_0) + '\n'
		text_file.write(line)

text_file.close()