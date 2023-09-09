n,h,m,k=input().split()
n=int(n)
m=int(m)//2
k=int(k)
M=[0]*m
T=['']*m
for i in range(n):
    a,b=input().split()
    b=int(b)%m
    if (b+k-1)>=m:
        for j in range((b+k)%m):
            T[j]=T[j]+str(i+1)+' '
            M[j]+=1
        for j in range(b+1, m):
            M[j]+=1
            T[j]=T[j]+str(i+1)+' '
    else:
        for j in range(b+1, b+k):
            M[j]+=1
            T[j]=T[j]+str(i+1)+' '
a1=min(M)
a2=M.index(a1)
print(a1,a2)
if a1>0:
    print(T[a2])
