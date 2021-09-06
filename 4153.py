while(1):
    a=[int(x) for x in input().split()]
    if a[0]==a[1] and a[1]==a[2] and a[2]==0:
        break
    a.sort()
    for i in range(0,3):
        a[i]=a[i]*a[i]
    if a[2]==(a[1]+a[0]):
        print("right")
    else:
        print("wrong")