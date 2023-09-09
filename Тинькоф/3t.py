n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=-1
for i in range(n):
    if a[i]!=b[i]:
        l=i
        break
if l==-1:
    f=0
else:
    r=-1
    for i in range(n-1,-1,-1):
        if a[i]!=b[i]:
            r=i
            break
    a=sorted(a[l:r+1])
    f=0
    for i in range(r-l+1):
        if a[i]!=b[i+l]:
            f=1
            break
if f==1:
    print('NO')
else:
    print('YES')
