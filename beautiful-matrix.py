b=[]
for i in range(5):
	l=raw_input()
	a=l.split()
	for j in range(5):
		b.append(a[j])
c=b.index('1')
i=(c)/5 + 1
j=(c)%5 +1
if i<=3:
	d=3-i
else:
	d=i-3

if j<=3:
	e=3-j
else:
	e=j-3

print d+e