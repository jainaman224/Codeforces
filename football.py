a=raw_input()

j=1
k=0
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        j+=1
        if j==7:
            k=1
    else:
        j=1
if k==1:
    print "YES"
else:
    print "NO"
