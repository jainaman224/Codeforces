a=int(raw_input())
b=int(raw_input())
c=int(raw_input())
d=int(raw_input())
e=int(raw_input())
j=0
for i in range(e):
    if ((i+1)%a)==0 or ((i+1)%b)==0 or ((i+1)%c)==0 or ((i+1)%d)==0:
        j+=1
print j