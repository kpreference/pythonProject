bur=[0,0,0]
ve=[0,0]
set=[]
cnt=5000
for i in range(0,3):
    bur[i]=int(input())
for i in range(0,2):
    ve[i]=int(input())
for i in range(0,2):
    for j in range(0,3):
        set.append(bur[j]+ve[i]-50)

set.sort()
print(set[0])