n=int(input())


for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    for k in range(2*(n-i)):
        print(" ",end="")
    for l in range(i):
        print("*",end="")
    print()
for m in range(n-1,0,-1):
    for o in range(m):
        print("*",end="")

    for p in range(2*(n-m)):
        print(" ",end="")

    for q in range(m):
        print("*",end="")
    print()


