s=[0]*3
for i in range(3):
    s[i]=[0]*2
    s[i][0]=list(map(int,input().split(":")))
    s[i][1]=(s[i][0][0]*60+s[i][0][1])*60+s[i][0][2]
if s[0][1]>s[2][1]:
    s[2][1]+=24*60*60
s[1][1]+=(s[2][1]-s[0][1]+1)//2
if s[1][1]>=24*60*60:
    s[1][1]-=24*60*60
s[1][0][0]=s[1][1]//(60*60)
s[1][0][1]=(s[1][1]//60)%60
s[1][0][2]=s[1][1]%60
for i in range(3):
    if i==2:
        if s[1][0][i]<10:
            print("0",s[1][0][i],sep="")
        else:
            print(s[1][0][i])
    else:
        if s[1][0][i]<10:
            print("0",s[1][0][i],sep="",end=":")
        else:
            print(s[1][0][i],end=":")

    
