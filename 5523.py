n=int(input())
cnt1=0
cnt2=0
for i in range(n):
    a,b=map(int,input().split())
    if a>b:
        cnt1+=1
    elif b>a:
        cnt2+=1

print(cnt1,cnt2)