a=int(raw_input())
j=0
for i in range(a):
    b=raw_input()
    c=[]
    c=b.split(' ')
    d=[]
    d=map(int, c)
    if (d[1]-d[0])>1:
        j+=1
print j