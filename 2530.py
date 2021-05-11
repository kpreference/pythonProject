a,b,c=map(int,input().split())
d=int(input())
tim=0
tim+=((a*3600)+(b*60)+c+d)

if tim>=86400:
    tim%=86400

h=int(tim/3600)

m=int(int(tim%(60*60))/60)

s=tim%60
print("%d %d %d"%(h,m,s))