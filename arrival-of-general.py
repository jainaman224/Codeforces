#!/usr/bin/python
a=int(raw_input())
b=raw_input()
c=b.split()
c=map(int, c)
d=max(c)
e=c.index(d)
c=c[::-1]
f=min(c)
g=c.index(f)
if a-1-g<e:
	h=e+g-1
else:
	h=e+g
print h