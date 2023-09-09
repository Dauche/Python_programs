s=input()
m=[0]*(ord("z")-ord("a")+1)
q=len(s)
for i in range(q):
    m[ord(s[i])-ord("a")]+=(q-i)*(i+1)
for i in range(ord("z")-ord("a")+1):
    if m[i]>0:
        print(chr(ord("a")+i),m[i],sep=": ")
