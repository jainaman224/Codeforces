#!/usr/bin/python
a=int(raw_input())
b=raw_input()
c=b.split()
c=map(int, c)
d=range(a)
for i in range(a):
	l=c[i]
	m=c[l-1]
	d[m-1]=l
for i in range(a):
	print d[i],