def brb(i,j):
    global A
    if A[i+1][j]=='.':
        A[i+1]=A[i+1][:j]+'U'+A[i+1][j+1:]
        brb(i+1,j)
    if A[i-1][j]=='.':
        A[i-1]=A[i-1][:j]+'D'+A[i-1][j+1:]
        brb(i-1,j)
    if A[i][j+1]=='.':
        A[i]=A[i][:j+1]+'L'+A[i][j+2:]
        brb(i,j+1)
    if A[i][j-1]=='.':
        A[i]=A[i][:j-1]+'R'+A[i][j:]
        brb(i,j-1)
    
N,M=input().split()
N=int(N)
M=int(M)
A=[0]*N
s0=0
ki=0
kj=0
for i in range(N):
    A[i]=input()
    if s0==0:
        for j in range(M):
            if A[i][j]=='S':
                s0+=1
                ki=i
                kj=j
brb(ki,kj)
ans_str="\n".join(A)
print(ans_str)

