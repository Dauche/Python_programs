import math
n,m,k=map(int,input().split())
s=[0]*n
s1=[0]*(n+1)
s2=[0]*(n+1)
s1[0]=[0]*(m+1)
s2[0]=[0]*(m+1)
for i in range(1,n+1):
    s[i-1]=list(map(int,input().split()))
    s1[i]=[0]*(m+1)
    s2[i]=[0]*(m+1)
    for j in range(1,m+1):
        s1[i][j]=s[i-1][j-1]+s1[i][j-1]
        s2[i][j]=s1[i][j]+s2[i-1][j]
for i in range(k):
    a1,b1,a2,b2=map(int,input().split())
    print(s2[a2][b2]+s2[a1-1][b1-1]-s2[a2][b1-1]-s2[a1-1][b2])
