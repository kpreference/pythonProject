import sys
e,s,m=map(int,sys.stdin.readline().split())
ee=0
ss=0
mm=0
cnt=0
while(1):
    cnt+=1
    ee+=1
    ss+=1
    mm+=1
    if ee==16:
        ee-=15
    if ss==29:
        ss-=28
    if mm==20:
        mm-=19
    if e==ee and s==ss and m==mm:
        break
print(cnt)