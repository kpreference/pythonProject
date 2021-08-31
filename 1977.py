def wj(x):
    cnt=0
    if x==1:
        cnt+=1
    else:
        for j in range(2,x):
            if x/(j*j)==1:
                cnt+=1
                break
    if cnt>0:
        return 1
    else:
        return 0

sum=0
cs=0
m=int(input())
n=int(input())
for i in range(m,n+1):
    if wj(i)==1:
        sum+=i
        if cs==0:
            cs=i
    else:
        pass
if sum>0:
    print(sum)
    print(cs)
else:
    print(-1)
