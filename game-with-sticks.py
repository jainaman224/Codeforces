#!/usr/bin/python
a=raw_input()
b=a.split()
c=map(int, b)
c.sort()
if c[0]%2==0:
	print "Malvika"
else:
	print "Akshat"