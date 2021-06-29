n,x=map(int,input().split())
a=[int(i) for i in input().split()]
for j in range(n):
    if a[j] < x :
        print(a[j],end=" ")