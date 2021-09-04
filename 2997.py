a=[int(x) for x in input().split()]

a.sort()
if (a[2]-a[1])==(a[1]-a[0]):
    print(a[2]+(a[1]-a[0]))
elif (a[2]-a[1])>(a[1]-a[0]):
    print(a[1]+(a[1]-a[0]))
elif (a[2]-a[1])<(a[1]-a[0]):
    print(a[0]+(a[2]-a[1]))