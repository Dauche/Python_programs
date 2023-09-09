n=int(input())
s=list(map(int,input().split()))
s.sort()
b=int(input())
m=list(map(int,input().split()))
m1=m.copy()
m1.sort()
l=dict()
i,j,z=0,0,0
while j<b:
    if i>=n:
        l[m1[j]]=z
        j+=1
    elif m1[j]>s[i]:
        if i+1>=n:
            i+=1
            z+=1
        elif s[i]==s[i+1]:
            i+=1
        else:
            i+=1
            z+=1
    else:
        l[m1[j]]=z
        j+=1
for i in m:
    print(l[i])
