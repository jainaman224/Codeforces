#!/usr/bin/python
a=int(raw_input())
x=0
for i in range(a):
	b=raw_input()
	if '++' in b:
		x+=1
	else:
		x-=1
print x