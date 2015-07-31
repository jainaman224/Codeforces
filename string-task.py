a=raw_input()
b=[]
for i in range(len(a)):
    b.append(a[i])
    if (ord(b[i])<91 and ord(b[i])>64):
        b[i]=chr(ord(b[i])+32)

str=""
l=0
while (l<len(b)):
    if b[l]=='a' or b[l]=='e' or b[l]=='i' or b[l]=='o' or b[l]=='u' or b[l]=='y' :
        b.remove(b[l])
        l-=1
    else:
        str=str+"."+b[l]
    l+=1
print str