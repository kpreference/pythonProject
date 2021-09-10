a=[1,1,2,2,2,8]
k,q,l,b,n,p=map(int,input().split())
a[0]-=k
a[1]-=q
a[2]-=l
a[3]-=b
a[4]-=n
a[5]-=p
for i in range(6):
    print("%d"%a[i],end=" ")


