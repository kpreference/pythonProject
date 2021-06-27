duf=[]
sum=0
for i in range(7):
    n=int(input())
    if n%2==1:
        duf.append(n)

if len(duf)==0:
    print(-1)
else:
    for j in range(len(duf)):
        sum+=duf[j]
    duf.sort()
    print(sum)
    print(duf[0])