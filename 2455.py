sum=0

m=0

for j in range(4):
    o,i=map(int,input().split())
    sum+=i
    sum-=o
    if sum>m:
        m=sum
print(m)