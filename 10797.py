n=int(input())

a=[int(x) for x in input().split()]
cnt=0
for i in range(5):
    if n==a[i]:
        cnt+=1
print(cnt)