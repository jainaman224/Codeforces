#!/usr/bin/python
a=raw_input()
b=a.split()
b=map(int, b)
d=raw_input()
c=d.split()
c=map(int, c)
c.sort()
d=1000000000
for i in range(b[1]-b[0]+1):
	if d > c[b[0]+i-1]-c[i]:
		d=c[b[0]+i-1]-c[i]
print d