n=int(input())
cnt=0
a=[int(x) for x in input().split()]
for i in range(n):
    if a[i]!=(i+1):
        cnt+=1
print(cnt)