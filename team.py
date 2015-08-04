a=int(raw_input())
l=0
for i in range(a):
    b=raw_input()
    c=[]
    c=b.split()
    k=0
    for j in range(3):
        if c[j]=='1':
            k+=1
    if k>1:
        l+=1
print l