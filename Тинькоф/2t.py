s=input()
d={'s':0,'h':0,'e':0,'r':0,'i':0,'f':0}
for i in s:
    if i in d:
        d[i]+=1
print(min(d['s'],d['h'],d['e'],d['r'],d['i'],d['f']//2))
