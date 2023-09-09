f1=open('the_calls.txt')
f2=open('calls.txt','w')
m=[line.split('\t') for line in f1]
m[-1][-1]=m[-1][-1]+'\n'
m.sort(key=lambda x: (x[2],(-1)*int(x[1])))
for i in range(len(m)-1):
    [f2.write(j+'\t') if j[-1]!='\n' else f2.write(j) for j in m[i]]
[f2.write(j+'\t') if j[-1]!='\n' else f2.write(j[:-1]) for j in m[-1]]
f1.close()
f2.close()
