n=int(input())
a,b=map(int,input().split())
a1,a2=a,a
b1,b2=b,b
for i in range(n-1):
    a,b=map(int,input().split())
    a1,a2=min(a,a1),max(a,a2)
    b1,b2=min(b,b1),max(b,b2)
print(a1,b1,a2,b2)
