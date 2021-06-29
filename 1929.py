def sosu(x):
    pan=0
    if x==1:
        return 1
    else:
        for i in range(2,x):
            if x%i==0:
                pan+=1
    return pan

a,b=map(int,input().split())

for i in range(a,b+1):
    if sosu(i)==0:
        print(i)