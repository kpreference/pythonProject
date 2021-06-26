n,m=map(int,input().split())
result=1
if n==m:
    print(1)
else:
    for i in range(n,n-m,-1):
        result*=i
    for j in range(1,m+1):
        result/=j
    print(int(result))