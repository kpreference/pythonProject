while(1):
    a=[int(x) for x in input().split()]
    if a[2]==a[1] and a[1]==a[0] and a[0]==0:
        break

    a.sort()
    if (a[0]+a[1])==a[2] or (a[0]+a[1])<a[2]:
        print("Invalid")
    elif (a[0]==a[1]) and (a[2]==a[1]) and (a[0]==a[2]) :
        print("Equilateral")
    elif (a[0]==a[1]) or (a[2]==a[1]):
        print("Isosceles")
    else:
        print("Scalene")

