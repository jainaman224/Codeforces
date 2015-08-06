#!/usr/bin/python
a=raw_input()
a=a.split(' ')
a=map(int, a)
b=a[2]*(a[2]+1)/2
c=a[0]*b
e=c-a[1]
if e>-1:
	print e
else:
	print '0'