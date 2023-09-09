n=int(input())
for j in range(n):
    s=input().split()
    m=[0]
    p=-1
    k=0
    for i in range(1,int(s[0])+1):
        a=float(s[i])
        if k==0:
            m.append(a)
            k+=1
        elif m[-1]>=a:
            m.append(a)
            k+=1
        else:
            if a>=p:
                while k!=0 and m[-1]<a:
                    p=m[-1]
                    m.pop()
                    k-=1
                m.append(a)
                k+=1
            else:
                k=-1
                break
    if k==0 or (m[-1]>=p and k!=-1):
        print(1)
    else:
        print(0)
