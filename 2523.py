n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()
i=0
j=0
for i in range(n):
    for j in range(n-i-1):
        print("*",end="")
    print()