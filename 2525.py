a,b=map(int,input().split())
c=int(input())
if(b+c>60):
    a+=int((b+c)/60)
    b+=(b+c)%60
    if(a>24):
        a-=24

else:
    b+=c
print("%d %d"%(a,b))






