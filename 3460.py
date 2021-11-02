nn=int(input())
for j in range(nn):

    n=int(input())

    cnt=0
    for i in range(len(str(bin(n))),2,-1):
        if int(str(bin(n))[i-1]) == 1:
            print(cnt,end=" ")
        cnt+=1



