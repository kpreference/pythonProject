n=int(input())
nn=[int(x) for x in input().split()]
sum=0
cnt=1

for i in range(n):
    if i==0:
       sum+=nn[i]
    else:
        if nn[i]==1:
            sum += 1
            if nn[i-1]==1:
                sum+=cnt
                cnt += 1
        elif nn[i]==0:
            cnt = 1
print(sum)
