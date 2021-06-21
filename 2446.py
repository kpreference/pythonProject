n=int(input())

for i in range(n):
    for k in range(i):
        print(" ",end="")
    for j in range(2*n-i*2-1):
        print("*", end="")
    k=0

    print()
i=0
j=0
k=0
for i in range(1,n):
    for k in range(n-i-1):
        print(" ",end="")
    for j in range(i*2+1):
        print("*",end="")


    print()


