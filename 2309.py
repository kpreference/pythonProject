a=[]
for i in range(9):
    aa=int(input())
    a.append(aa)

a.sort()
sum=0
for i in range(0,9):
    for j in range(i+1,9):
        sum=0
        for k in range(0,9):
            if k!=i and k!=j:
                sum+=a[k]
        if sum==100:
            del a[i]
            del a[j-1]
            break
for m in range(7):
    print(a[m])


