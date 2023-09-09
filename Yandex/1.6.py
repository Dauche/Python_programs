m=int(input())
n=int(input())
s1=[]
s2=[]
k=0
for i in range(n):
    a,b=map(int,input().split())
    j=0
    f=0
    while j<k and f==0:
        if s1[j]<a:
            j+=1
        else:
            f=1
    if j!=0:
        if s2[j-1]>=a:
            j=j-1
            s1.pop(j)
            s2.pop(j)
            k-=1
    while j<k and f!=2:
        if s1[j]<=b:
            s1.pop(j)
            s2.pop(j)
            k-=1
        else:
            f=2
    s1.insert(j,a)
    s2.insert(j,b)
    k+=1
print(k)
            
            
    
