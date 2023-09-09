f=open('input.txt')
d=dict()
s=[]
mk=1
for line in f:
    for i in line:
        if i!="\n" and i!=" ":
            if d.get(i,0)==0:
                s.append(i)
                d[i]=1
            else:
                d[i]+=1
                mk=max(mk,d[i])
s.sort()
for i in range(mk,0,-1):
    for j in s:
        if i>d[j]:
            print(" ", end='')
        else:
            print("#",end='')
    print()
[print(i,end='') for i in s]
f.close()
