n,m=map(int,input().split())
gl=[i for i in range(n+1)]
chl=[0]*(n+1)
sp=[[] for i in range(n+1)]
for i in range(m):
    k=list(map(int,input().split()))
    if k[0]==1:
        if gl[k[1]]!=gl[k[2]]:
            if len(sp[gl[k[1]]])<len(sp[gl[k[2]]]):
                k[1],k[2]=k[2],k[1]
            vr=gl[k[2]]
            chl[vr]-=chl[gl[k[1]]]
            for j in sp[vr]:
                chl[j]+=chl[vr]
                gl[j]=gl[k[1]]
            sp[vr].append(vr)
            sp[gl[k[1]]].extend(sp[vr])
            gl[vr]=gl[k[1]]
            sp[vr]=[]
            chl[gl[k[1]]]+=1
    elif k[0]==2:
        if gl[k[1]]==gl[k[2]]:
            print('YES')
        else:
            print('NO')
    elif k[0]==3:
        if gl[k[1]]==k[1]:
            print(chl[k[1]]+1)
        else:
            print(chl[k[1]]+chl[gl[k[1]]]+1)
    
