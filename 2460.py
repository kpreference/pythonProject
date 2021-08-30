peo=0
maxpeo=0
for i in range(10):
    n,t=map(int,input().split())
    peo-=n
    peo+=t

    if peo>maxpeo:
        maxpeo=peo

print(maxpeo)