a=raw_input()
b=a.find('h')
while b<len(a) and a[b]!='e':
	b+=1
b+=1
while b<len(a) and a[b]!='l':
	b+=1
b+=1
while b<len(a) and a[b]!='l':
	b+=1
b+=1
while b<len(a):
	if a[b]=='o':
		break
	b+=1

if b<len(a):
	print "YES"
else:
	print "NO"