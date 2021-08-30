n=int(input())

for i in range(n):
    a,b=input().split()

    for j in range(len(b)):
        if j!=(int(a)-1):
            print(b[j],end="")
    print()
