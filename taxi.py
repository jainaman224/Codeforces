a=int(raw_input())
b=raw_input().split(" ")
b.sort(reverse = True)
b=map(int, b)

k=0
i=0
j=a-1

while i<=j:
    k+=1
    l=4-b[i]
    while (b[j]<=l) and (j>=i):
        l-=b[j]
        j-=1
    i+=1

print k