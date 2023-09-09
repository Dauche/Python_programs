s=list(map(int,input().split()))
s1=[0]*(s[0]+1)
s2=[0]*(s[0]+1)
m=[[0,0]]
for i in range(1,s[0]+1):
    if m[-1][0]<=s[i]:
        m.append([s[i],i])
    else:
        while m[-1][0]>s[i]:
            s1[m[-1][1]]=i
            m.pop()
        m.append([s[i],i])
while m[-1]!=[0,0]:
    s1[m[-1][1]]=s[0]+1
    m.pop()
for i in range(s[0],0,-1):
    if m[-1][0]<=s[i]:
        m.append([s[i],i])
    else:
        while m[-1][0]>s[i]:
            s2[m[-1][1]]=i
            m.pop()
        m.append([s[i],i])
while m[-1]!=[0,0]:
    s2[m[-1][1]]=0
    m.pop()
mk=0
for i in range(1,s[0]+1):
    mk=max(mk,(s1[i]-s2[i]-1)*s[i])
print(mk)
