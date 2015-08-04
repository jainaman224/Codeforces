a=raw_input()
j=0
if (int(a)%4)==0 or (int(a)%7)==0 or (int(a)%47)==0 or (int(a)%74)==0 or (int(a)%447)==0 or (int(a)%477)==0 or (int(a)%774)==0:
    print "YES"
else:
    for i in range(len(a)):
        if a[i]=='4' or a[i]=='7':
            j+=1
    if j==len(a):
        print "YES"
    else:
        print "NO"