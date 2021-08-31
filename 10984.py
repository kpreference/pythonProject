n=int(input())
for i in range(n):
    h=0
    p=0
    m=int(input())
    for j in range(m):
        c,g=input().split()
        h+=int(c)
        p+=(float(g)*float(c))
    print("%d %.2f"%(h,p/h))