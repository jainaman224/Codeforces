#!/usr/bin/python
a=raw_input()
b=a.split()
c=map(int, b)
d=c[0]
f=c[1]
while c[0]>=c[1]:
	e=c[0]/c[1]
	f=c[0]%c[1]
	c[0]=e+f
	d+=e
print d
