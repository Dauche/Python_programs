n,s=map(int,input().split())
mas=list(map(int,input().split()))
otv=0
for i in mas:
    if s>=i and i>otv:
        otv=i
print(otv)
