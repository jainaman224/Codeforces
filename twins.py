a=int(raw_input())
b=raw_input()
c=b.split()
d=map(int,c)
d.sort()
sum=0
for i in range(a):
    sum+=d[i]

su=0
j=0
for i in range(a):
    if su<=sum:
        su+=d[a-i-1]
        sum-=d[a-i-1]
        j+=1
print j