a=raw_input()
b=raw_input()
c=a.split()
d=int(c[0])
e=int(c[1])
f=b.split()
g=map(int,f)
j=0
h=g[e-1]
for i in range(d):
    if g[i]>0:
        if g[i]>=h:
            j+=1

print j