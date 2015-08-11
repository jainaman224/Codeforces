#!/usr/bin/python
from __future__ import division
from math import sqrt


a=raw_input().split(' ')
a=map(int, a)

b=a[0]/a[1]

m=1
c=1
d=2



for i in xrange(3,2000000):
	t=0
	if (i%2!=0):
		# To check whether no. is prime or not
		for j in xrange(3,int(sqrt(i))+2,2):
			if (i%j==0):
				t=1
				break
		if(t==0):
			c+=1
			# checking whether desired condition is true or not
			if( c>(b*d) and (c-1)<=(b*d) ):
				m=i-1


	s=str(i)
	# To check whether no. is palindrome or not
	if (s==s[::-1]):
		d+=1
		# checking whether desired condition is true or not
		if( c<=(b*d) ):
			m=i

print m