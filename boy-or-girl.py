a=raw_input()
b=list(a)
b.sort()
j=1
for i in range(len(a)-1):
    if b[i]!=b[i+1]:
        j+=1
if (j%2)==0:
    print "CHAT WITH HER!"
else:
    print "IGNORE HIM!"