a=raw_input()
b=a.split()
b.sort()
j=0
for i in range(3):
	if b[i]!=b[i+1]:
		j+=1
print 3-j