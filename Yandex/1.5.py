n=int(input())
z=0
a=int(input())
for i in range(n-1):
    b=int(input())
    z+=min(a,b)
    a=b
print(z)
