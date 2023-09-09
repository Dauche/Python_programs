s=input()
n1=0
n2=0
n3=0
k=[0]*(ord('z')-ord('a')+1)
for i in s:
    if i=='<':
        n1+=1
    elif i=='>':
        n2+=1
    elif i=='/':
        n3+=1
    else:
        k[ord(i)-ord('a')]+=1
f=0
for i in range(len(k)):
    if k[i]%2!=0:
        if f=0:
            a=i
            f+=1
        else:
            b=i
            f+=1
if f==0:
    f1=0
    for i in range(len(s)):
        if s[i]
