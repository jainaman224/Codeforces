a=raw_input()
j=0
for i in range(len(a)):
    if a[i]=='4' or a[i]=='7':
        j+=1

if j==4 or j==7:
    print "YES"
else:
    print "NO"