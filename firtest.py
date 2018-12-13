x = [0,0,0,0]
def inc_x():
	x[0] += 1
	if x[0] > 15:
		x[0] = 0
def trunc_6(n):
	b = bin(n)
	if len(b) > 8:
		new = b[len(b)-6:]
		new = int(new,2)
	else:
		return n
	return new


in_file = open('fir.vec','r')
text_file = open('firtest.vec','w')
intermed1 = [0,0,0,0]
intermed2 = [0,0]
for i in range(0,22):
	text_file.write(in_file.readline())

for b0 in range(0,16):
	for b1 in range(0,16):
		for b2 in range(0,16):
			for b3 in range(0,16):
				b = [b0,b1,b2,b3]
				for i in [3,2,1]:
					x[i] = x[i-1]
				inc_x()
				for i in range(0,4):
					intermed1[i] = trunc_6(x[i]*b[i])
				for i in range(0,2):
					intermed2[i] = trunc_6(intermed1[2*i] + intermed1[2*i+1])
				output = trunc_6(intermed2[0] + intermed2[1])
				outputhex = '{0:01x}'.format(output)
				outputhi = '0'
				outputlo = '0'
				if len(outputhex) > 1:
					outputhi = outputhex[0]
					outputlo = outputhex[1]
				else:
					outputhi = '0'
					outputlo = outputhex
				line1 = '{0:01x} {1:01x} {2:01x} {3:01x} {4:01x} 0 x x\n'.format(x[0], b[0], b[1], b[2], b[3])
				line2 = '{0:01x} {1:01x} {2:01x} {3:01x} {4:01x} 1 {5:s} {6:s}\n'.format(x[0], b[0], b[1], b[2], b[3],outputhi, outputlo)
				text_file.write(line1)
				text_file.write(line2)
				text_file.write(';'+str(x) + '\n' )

text_file.close()
