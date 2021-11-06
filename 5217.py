n=int(input())
for i in range(n):
    m=int(input())
    print("Pairs for %d:"%m,end="")
    cnt=0
    for j in range(1,int(m/2+1)):

        if j != m-j:
            if cnt > 0:
                print(",", end="")
            print(" %d %d"%(j,m-j),end="")
            cnt+=1
    print()