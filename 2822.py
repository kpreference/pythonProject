a=[]
m1=151
m2=151
m3=151
mm=0
for i in range(8):
    n=int(input())
    a.append(n)

for j in range(8):
    if a[j]<m1:
        m1=a[j]

for k in range(8):
    if a[j]<m2:
        if m1<m2:
            m2=a[j]
for l in range(8):
    if a[j]<m3:
        if m2<m3:
            m3=a[j]
sum=0
for m in range(8):
    if a[m]!=m1 or a[m]!=m2 or a[m]!=m3:
        sum+=a[m]
print(sum,m1,m2,m3)
for q in range(8):
    if a[q]!=m1 or a[q]!=m2 or a[q]!=m3:
        print("%d"%(q+1),end=" ")
