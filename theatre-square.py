f=raw_input()
g=f.split()
a=int(g[0])
b=int(g[1])
c=int(g[2])

d=int(a/c)
e=int(b/c)

if ((a%c)!=0):
	d+=1
if ((b%c)!=0):
	e+=1

print (d*e)