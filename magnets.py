#!/usr/bin/python
a=int(raw_input())
c=[]
for i in range(a):
	b=int(raw_input())
	c.append(b)
j=1
for i in range(a-1):
	if c[i]!=c[i+1]:
		j+=1
print j