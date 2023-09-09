def inou():
    global k1,k2
    m1.append(m2[-1])
    k1+=1
    m2.pop()
    k2-=1
def sk(n):
    global k1,k2,f
    if n=='(':
        m2.append(n)
        k2+=1
    elif n==')':
        while m2[-1]!='(' and k2!=1:
            inou()
        if k2==1 and m2[-1]!='(':
            f=3
        else:
            m2.pop()
            k2-=1
    elif n=='*':
        while m2[-1]=='*':
            inou()
        m2.append(n)
        k2+=1
    else:
        while m2[-1] in n1cis:
            inou()
        m2.append(n)
        k2+=1
    
s=input()
cis=['0','1','2','3','4','5','6','7','8','9']
ncis=['(',')','*','+','-']
n1cis=['*','+','-']
m1=[0]
m2=[0]
f=0
f1=0
k1=0
k2=0
for i in s:
    if f==0:
        if i in cis:
            a=i
            f=1
            f1=0
        elif i in ncis:
            if i in n1cis:
                f1+=1
            sk(i)
        elif i!=' ':
            f=3
    elif f==1:
        if i in cis:
            a+=i
        elif i in ncis:
            if i in n1cis:
                f1+=1
            f=0
            m1.append(int(a))
            k1+=1
            sk(i)
        elif i==' ':
            f=2
        else:
            f=3
    elif f==2:
        if i in ncis:
            if i in n1cis:
                f1+=1
            f=0
            m1.append(int(a))
            k1+=1
            sk(i)
        elif i!=' ':
            f=3
    if f==3 or f1>1:
        break
if f==3 or f1>0:
    print('WRONG')
else:
    if f!=0:
        f=0
        m1.append(int(a))
        k1+=1
    while k2!=0 and m2[-1]!='(':
        inou()
    if k2!=0:
        f=1
    m3=[0]
    k3=0
    for i in range(1,k1+1):
        if f==1:
            break
        if m1[i] in n1cis:
            if k3>=2:
                a,b=m3[-1],m3[-2]
                m3.pop()
                m3.pop()
                k3-=1
                if m1[i]=='+':
                    m3.append(a+b)
                elif m1[i]=='-':
                    m3.append(b-a)
                else:
                    m3.append(a*b)
            else:
                f=1
        else:
            m3.append(m1[i])
            k3+=1
    if k3!=1:
        f=1
    if f==1:
        print('WRONG')
    else:
        print(m3[-1])
            
