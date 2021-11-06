while(1):
    a,b=map(int,input().split())
    if a==b and a==0:
        break
    cnt=0
    while(a!=0 and b!=0):
        by=(a%10)+(b%10)
        if by>9:
            cnt+=1
        a=int(a/10)
        b=int(b/10)
        print(a,b)
    print(cnt)