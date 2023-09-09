k=int(input())
s=input()
d=dict()
lens=len(s)
z=k+1
if z>=lens:
    z=lens
for i in s:
    d[i]=d.get(i,0)+1
for q in range(ord("z")-ord("a")+1):
    j=chr(ord("a")+q)
    if d.get(j,0)!=0:
        if d[j]+k>=lens or z==lens:
            z=lens
        elif d[j]+k>z:
            p=0
            i=0
            while i<k+p:
                if s[i]==j:
                    p+=1
                i+=1
            t=0
            z=max(z,p+k)
            while i<lens:
                if s[i]==j:
                    p+=1
                    z=max(z,p+k)
                elif s[t]==j:
                    while s[t]==j:
                        t+=1
                        p-=1
                    t+=1
                else:
                    t+=1
                i+=1
print(z)
            
            
