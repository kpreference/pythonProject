n=int(input())
for i in range(n):
    pr=0
    pl=""
    p=int(input())
    for j in range(p):
        prr,pll=input().split(" ")
        if int(prr)>pr:
            pr=int(prr)
            pl=pll
    print(pl)