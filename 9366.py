n=int(input())
for i in range(n):
    a=[int(x) for x in input().split()]
    a.sort()
    if (a[0]+a[1])==a[2] or (a[0]+a[1])<a[2]:
        print("Case #%d: invalid!"%(i+1))
    elif (a[0]==a[1]) and (a[2]==a[1]) and (a[0]==a[2]) :
        print("Case #%d: equilateral"%(i+1))
    elif (a[0]==a[1]) or (a[2]==a[1]):
        print("Case #%d: isosceles" % (i + 1))
    else:
        print("Case #%d: scalene" % (i + 1))

