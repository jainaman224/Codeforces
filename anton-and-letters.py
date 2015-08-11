#!/usr/bin/python
a=raw_input()
a=a.strip(',')
b=list(a)
b.sort()
c=0
for i in range(len(b)):
	#counting no. of distinct letters only alphabets that is excluding braces comma and space character.
	if(b[i]!='{' and b[i]!='}' and b[i]!=',' and b[i]!=' '):
		if (b[i]!=b[i-1]):
			c+=1
print c