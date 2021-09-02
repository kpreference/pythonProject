a=[0,0,0,0,0]
sum=0
for i in range(5):
    a[i]=int(input())
    sum+=a[i]

a.sort()
print("%d"%(sum/5))
print(a[2])