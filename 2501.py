yak=[]

n,k=map(int,input().split())
for i in range(1,n+1):
    if n%i==0:
        yak.append(i)

if len(yak)>=k:
    print(yak[k-1])
else:
    print(0)