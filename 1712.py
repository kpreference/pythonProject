a,b,c=map(int,input().split())

hand=0
if b>c or b==c:
    print(-1)
else:
    bene = c - b
    hand=a//bene
    print(hand+1)
