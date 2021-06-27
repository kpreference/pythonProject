a,b=map(int,input().split())

duf=[]
sum=0
for i in range(b+1):
    for j in range(i):
        duf.append(i)

for i in range(a,b+1):
    sum+=duf[i-1]
print(sum)