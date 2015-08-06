#!/usr/bin/python
a=int(raw_input())
b=int(raw_input())
c=int(raw_input())
d=[]
d.append(a*b*c)
d.append((a+b)*c)
d.append((c+b)*a)
d.append(a+b+c)
e=max(d)
print e