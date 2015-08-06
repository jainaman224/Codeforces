#!/usr/bin/python
a=raw_input()
b=raw_input()
c=""
for i in range(len(a)):
	if((a[i]=='1' and b[i]=='0')or(a[i]=='0' and b[i]=='1')):
		c+='1'
	else:
		c+='0'
print c