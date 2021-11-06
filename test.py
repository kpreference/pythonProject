fac=1
n=int(input())
cnt=0

for i in range(1,n+1):
    fac*=i
    if fac%10==0:
        cnt+=1
        fac/=10

print(cnt)