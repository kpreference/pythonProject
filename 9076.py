n=int(input())
for i in range(n):

    a=[int(x) for x in input().split()]
    a.sort()
    if (a[3]-a[1])>3:
        print("KIN")
    else:
        print("%d"%(a[1]+a[2]+a[3]))
