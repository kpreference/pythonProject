def sosu(x):
    pan=0
    if x==1:
        return 1
    else:
        for i in range(2,x):
            if x%i==0:
                pan+=1
    return pan

m=int(input())
n=int(input())

sum=0
ch=0
cnt=0

for i in range(m,n+1):
    if sosu(i)>0:
        pass
    else:
        sum+=i
        if ch==0:
            ch=i
        cnt+=1

if cnt>0:
    print(sum)
    print(ch)
else:
    print(-1)
