a=raw_input()
str=""

j=0
for i in range(len(a)-1):
    if ord(a[i+1])<91 and ord(a[i+1])>64:
        j+=1
        
if j==(len(a)-1):
    if ord(a[0])<91 and ord(a[0])>64:
        str=str+chr(ord(a[0])+32)
    else:
        str=str+chr(ord(a[0])-32)
    for k in range(len(a)-1):
        if ord(a[k+1])<91 and ord(a[k+1])>64:
            str=str+chr(ord(a[k+1])+32)
else:
    for k in range(len(a)):
        str=str+chr(ord(a[k]))
print str