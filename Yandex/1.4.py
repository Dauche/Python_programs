n=int(input())
k=int(input())
r=int(input())
p=int(input())
q=(r-1)*2+p
if (q+k)>n and (q-k)<1:
    print(-1)
elif (q+k)>n or (p==2 and k%2==1 and (q-k)>=1):
    print((q-k+1)//2,(p+k+1)%2+1)
else:
    print((q+k+1)//2,(p+k+1)%2+1)
    
