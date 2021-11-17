def ijin(x):
    a=0
    b=0

n=int(input())
for k in range(n):
    a,b=input().split()
    cnt1=0
    cnt2=0
    for i in range(0,len(a)):
        if int(a[len(a)-1-i])==1:
            cnt1+=(2**i)
    for j in range(0,len(b)):
        if int(b[len(b)-1-j])==1:
            cnt2+=(2**j)
    #print(cnt1,cnt2)
    for m in range(2,len(str(bin(cnt1+cnt2)))):
        print(str(bin(cnt1+cnt2))[m],end="")
    print()

