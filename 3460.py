n=int(input())
for i in range(n):
    a=int(input())
    for j in range(2,len(str(bin(a)))):
        if str(bin(a))[j]==1:
            print(j-2,end=" ")
    print()
