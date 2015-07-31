a=int(raw_input())
for i in range(a):
    b=raw_input()
    str=""
    d=len(b)-2
    c=d.__str__()
    if len(b)<11:
        str=b
    else:
        str=b[0]+c+b[(len(b)-1)]
    print str
