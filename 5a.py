n=int(input())
a=list(map(int,input().split()))
p=[0]*(n+1)
d={0:[0]}
m=[]
ans=0
for i in range(1,n+1):
    p[i]=p[i-1]+a[i-1]
    if d.get(p[i],0)==0:
        d[p[i]]=[i]
    else:
        d[p[i]].append(i)
for j in d.keys():
    for i in range(1,len(d[j])):
        m.append([d[j][i-1],d[j][i]])
m.sort()
if len(m)!=0:
    l=[m[-1]]
else:
    l=[]
for i in range(len(m)-2,-1,-1):
    if m[i][1]<l[-1][1]:
        l.append(m[i])
r=n
for i in l:
    ans+=(i[0]+1)*(r-i[1]+1)
    r=i[1]-1
print(ans)
