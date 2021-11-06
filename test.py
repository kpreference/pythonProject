import math
cnt=0
while(1):
    cnt+=1
    a,b,c=map(int,input().split())
    if a==b and b==c and a==0:
        break
    print("Triangle #%d"%cnt)

    if c==(-1):
        print("c = %.3f"%(math.sqrt(a*a+b*b)))
    elif b==(-1):
        if a==c or a>c:
            print("Impossible.")
        else:
            print("b = %.3f" % (math.sqrt(c*c - a*a)))
    elif a==(-1):
        if b==c or b>c:
            print("Impossible.")
        else:
            print("a = %.3f" % (math.sqrt(c*c - b*b)))


    print()