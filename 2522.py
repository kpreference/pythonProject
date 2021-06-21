n=int(input())
for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")

    print()
i=0
j=0
k=0
for i in range(1,n):
    for k in range(i):
        print(" ",end="")
    for j in range(n-i):
        print("*",end="")
    print()