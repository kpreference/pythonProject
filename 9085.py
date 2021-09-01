n=int(input())
sum=0
for i in range(n):
    sum=0
    a=int(input())
    aa=[int(x) for x in input().split()]
    for j in range(a):
        sum+=aa[j]
    print(sum)