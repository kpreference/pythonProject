n=int(input())
for i in range(n):
    a=int(input())
    for j in range(2, len(str(bin(a)))):
        aa=str(bin(a))[j]
        print(str(bin(a))[j],aa)
        print(j-2)
        if aa==1:
            print("%d"%(j-2),end=" ")

    print()
