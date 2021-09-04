n=int(input())
for i in range(n):
    che=101
    sum=0
    a=[int(x) for x in input().split()]
    for j in range(7):
        if a[j]%2==0:
            sum+=a[j]
            if che>a[j]:
                che=a[j]
    print(sum,che)