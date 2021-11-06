def sosu(x):
    for i in range(2,x):
        if x%i==0:
            return 0
        if i*i<=x:
            break
    return 1
a,b=map(int,input().split())
for j in range(len(str(a))):
    b*=10
b+=a

if sosu(a)==1 and sosu(b)==1:
    print("Yes")
else:
    print("No")