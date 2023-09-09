def count(mapg,n,gr):
    vis=[1]*(n+1)
    ans=0
    for i in range(1,n+1):
        if vis[i]:
            ans+=1
            f(mapg,vis,i,gr)
    return ans

def f(mapg,vis,i,gr):
    vis[i]=0
    for j in mapg[i]:
        if vis[j[0]] and j[1]>gr:
            f(mapg,vis,j[0],gr)
                 
n,m=map(int,input().split())
l=1000000001
r=-1
spg=[[]]*(n+1)
for i in range(m):
    g1,g2,weigth=map(int,input().split())
    if g1!=g2:
        spg[g2].append([g1,weigth])
        spg[g1].append([g2,weigth])
        l=min(l,weigth)
        r=max(r,weigth)
st=count(spg,n,-1)
l-=1
r+=1
while r-l>1:
    sr=(l+r)//2
    if st<count(spg,n,sr):
        r=sr-1
    else:
        l=sr+1
print(l)
