a=raw_input()
j=0
c=[]
d=[]
str=""
for i in range((len(a)+1)/2):
    c.append(int(a[2*i]))
for i in range(len(c)):
    j=i
    b=c[i]
    while j<(len(c)):
        if b>c[j]:
            e=b
            b=c[j]
            c[j]=e
        j+=1
    d.append(b.__str__())
    
for i in range(len(d)-1):
    str=str+d[i]+"+"
str+=d[len(d)-1]
print str