n,m=map(int,input().split())
a=list(map(int,input().split()))
f=0
for i in range(1,3**m):
    s=i
    k=0
    p=0
    while s>0:
        p+=a[k]*(s%3)
        k+=1
        s=s//3
    if p==n:
        s=i
        f=1
        break
if f==1:
    k=0
    l=[]
    while s>0:
        h=s%3
        if h==2:
            l.append(a[k])
            l.append(a[k])
        elif h==1:
            l.append(a[k])
        k+=1
        s=s//3
    print(len(l))
    print(*l)
else:
    print(-1)
