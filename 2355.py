a,b=map(int,input().split())
if b>a:
    sum=((a+b)*(b-a+1))/2
    print("%d"%sum)
elif a>b:
    sum = ((a + b) * (a - b + 1)) / 2
    print("%d" % sum)