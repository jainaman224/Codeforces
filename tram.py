a=int(raw_input())
l=0
k=0
for i in range(a):
    b=raw_input()
    c=[]
    d=[]
    d=b.split()
    c=map(int,d)
    k=k-c[0]+c[1]
    if k>l:
        l=k
print l