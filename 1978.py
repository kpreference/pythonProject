def sosu(x):
    pan=0
    if x==1:
        return 1
    else:
        for i in range(2,x):
            if x%i==0:
                pan+=1
    return pan

n=int(input())
cnt=0
a=[int(i) for i in input().split()]

for j in range(n):
    if sosu(a[j])==0:
        cnt+=1
print(cnt)