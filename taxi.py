#/usr/bin/python
a=int(raw_input())
b=raw_input()
c=b.split()
c=map(int, c)
c.sort()
j=0
i=1
while i <= a:
	
	if c[a-i]==4:
		j+=1
		c.remove(c[a-i])
	else:
		k=0
		while k < (a-i):
			if c[a-i]+c[k]<4:
				l=k+1
				while l < a-i:
					if c[a-i]+c[k]+c[l]<4:
						j+=1
						m=l+1
						while m < (a-i):
							if c[a-i]+c[k]+c[l]+c[m]==4:
								c.remove(c[a-i])
								c.remove(c[m])
								c.remove(c[l])
								c.remove(c[k])
								i+=3
								m=a+5
								k=a+5
								l=a+5
							m+=1
						if k<a+1:
							c.remove(c[a-i])
							c.remove(c[l])
							c.remove(c[k])
							i+=2
							k=a+5
							l=a+5
					elif c[a-i]+c[k]+c[l]==4:
						c.remove(c[a-i])
						c.remove(c[l])
						c.remove(c[k])
						j+=1
						i+=2
						k=a+5
						l=a+5
					l+=1
				if k<a+1:
					j+=1
					i+=1
					c.remove(c[a-i])
					c.remove(c[k])
					k=a+5
			elif c[a-i]+c[k]==4:
				j+=1
				c.remove(c[a-i])
				c.remove(c[k])
				i+=1
				k=a+5
			k+=1
		if k<a+1:
			j+=1
			c.remove(c[a-i])
	i+=1
print j