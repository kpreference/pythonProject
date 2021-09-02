n=int(input())
a=[]
for i in range(n):
    aa=int(input())
    a.append(aa)
a.sort()
for j in range(n):
    if j!=0:
        if a[j]!=a[j-1]:
            print(a[j])
    elif j==0:
        print(a[j])
