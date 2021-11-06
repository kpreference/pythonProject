n=int(input())
if n==2:
    a,b=map(int,input().split())
    if b<a:
        b,a=a,b

    for i in range(1,a+1):
        if a%i==0 and b%i==0:
            print(i)
else:
    a,b,c=map(int,input().split())
    min=a
    if min>b:
        min=b
    if min>c:
        min=c
    for i in range(1,min+1):
        if a%i==0 and b%i==0 and c%i==0:
            print(i)