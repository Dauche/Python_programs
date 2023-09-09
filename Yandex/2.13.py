def inou():
    global k
    m1.append(m2[-1])
    m2.pop()
    k-=1

s=input()
ncis=['(',')','!','&','|','^']
n1cis=['!','&','|','^']
n2cis=['!','&']
m1=[]
m2=[]
k=0
for i in s:
    if i in ncis:
        if i=='(':
            m2.append(i)
            k+=1
        elif i==')':
            while m2[-1]!='(':
                inou()
            m2.pop()
            k-=1
        elif i=='!':
            while k>0 and m2[-1]=='!':
                inou()
            m2.append(i)
            k+=1
        elif i=='&':
            while k>0 and m2[-1] in n2cis:
                inou()
            m2.append(i)
            k+=1
        else:
            while k>0 and m2[-1] in n1cis:
                inou()
            m2.append(i)
            k+=1
    else:
        m1.append(int(i))
while k!=0:
    inou()
m3=[]
for i in m1:
    if i in n1cis:
        if i=='!':
            a=m3[-1]
            m3.pop()
            m3.append((a+1)%2)
        else:
            a,b=m3[-1],m3[-2]
            m3.pop()
            m3.pop()
            if i=='&':
                m3.append(a*b)
            elif i=='|':
                m3.append(max(a,b))
            else:
                m3.append(max(a,b)-min(a,b))
    else:
        m3.append(i)
print(m3[-1])
