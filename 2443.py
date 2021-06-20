n=int(input())

for i in range(1,n+1):

    for k in range(0,i-1):
        print(" ",end="")


    for j in range((n+1-i)*2-1,0,-1):
        print("*",end="")
    print()