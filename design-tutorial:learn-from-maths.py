#!/usr/bin/python
import math
def isNotPrime(num):
	if num%2==0:
		return True
	else:
		for i in range(3,int(math.sqrt(num))+1,2):
			if num%i==0:
				return True
	return False

a=int(raw_input())
b=a/2
c=a-b
i=0
while i < a/2:
	if ((isNotPrime(b)) and (isNotPrime(c))):
		break
	else:
		b-=1
		c+=1
		i+=1

print b,c