a=raw_input()
j=0
for i in range(len(a)):
	if a[i]=='H' or a[i]=='Q' or a[i]=='9':
		j=1
if j==1:
	print "YES"
else :
	print "NO"