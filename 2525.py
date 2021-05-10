a,b=map(int,input().split())
c=int(input())
w=a*60+b+c
a=int(w/60)
if(a>23):
    a-=24
b=w%60
print("%d %d"%(a,b))






