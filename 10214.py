n=int(input())
for i in range(n):
    ys=0
    ks=0
    for j in range(9):
        y,k=map(int,input().split())
        ys+=y
        ks+=k

    if ys>ks:
        print("Yonsei")
    elif ks>ys:
        print("Korea")
    else:
        print("Draw")
