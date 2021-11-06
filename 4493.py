n=int(input())
for i in range(n):
    m=int(input())
    cnt1=0
    cnt2=0
    for j in range(m):
        p1,p2=input().split()
        if p1==p2:
            cnt1+=1
            cnt2+=1
        elif (p1=='R' and p2=='P' ) or (p1=='S' and p2=='R' ) or (p1=='P' and p2=='S' ):
            cnt2+=1
        else:
            cnt1+=1

    if cnt1>cnt2:
        print("Player 1")
    elif cnt1<cnt2:
        print("Player 2")
    else:
        print("TIE")