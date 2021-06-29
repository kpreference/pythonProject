n=int(input())
b10=0
b60=0
b300=0
if n%10 != 0:
    print(-1)
else:
    while(n!=0):
        if n>=300:
            n-=300
            b300+=1
        elif n>=60:

            n-=60
            b60+=1
        elif n>=10:
            n-=10
            b10+=1
    print("%d %d %d" % (b300, b60, b10))

