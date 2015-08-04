a=raw_input()
i=0
c=int(a)+1
while i!=1:
    d=list(c.__str__())
    d.sort()
    k=0
    for j in range(3):
        if (d[j]!=d[j+1]):
            k+=1
    if k==3:
        print c
        i=1
    else:
        c+=1