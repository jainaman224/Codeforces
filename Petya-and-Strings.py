a=raw_input()
b=raw_input()
a=a.upper()
b=b.upper()
e=[]
e.append(a)
e.append(b)
e.sort()
if a==b:
    print '0'
elif a==e[0]:
    print '-1'
else:
    print '1'