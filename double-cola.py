#!/usr/bin/python
a=int(raw_input())
d=0
i=0
while d<a:
	b=d
	d+=5*(2**i)
	i+=1
i=i-1
c=0
while (b<a):
	b+=2**(i)
	c+=1

if c==0 or c==5:
	print "Howard"
elif c==1:
	print "Sheldon"
elif c==2:
	print "Leonard"
elif c==3:
	print "Penny"
else:
	print "Rajesh"
