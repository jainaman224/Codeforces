#!/usr/bin/python
a=raw_input().split(' ')
a=map(int, a)
c=raw_input()
b=list(c)
d=""

while (a[1]>0):
	i=0
	while i<(len(b)-1):
		#to check if 'G' is standing behind 'B',If yes thn swap their positions
		if (b[i]=='B' and b[i+1]=='G'):
			b[i],b[i+1]=b[i+1],b[i]
			#as i and i+1 as swapped so it vl be 'B' therefore there is a need to increment
			i+=1
		i+=1
	a[1]-=1

for i in range(len(b)):
	d+=b[i]

print d

