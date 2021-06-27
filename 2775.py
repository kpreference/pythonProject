def peocnt(k,n):
    i=0
    global sum
    if k==1:
        i=0
        for i in range(n+1):
            sum+=i
    else:
        i=0
        for i in range(1,k+1):
            peocnt(k,n)



sum=0

a=int(input())
for j in range(a):
    sum=0
    b=int(input())
    c=int(input())
    peocnt(b,c)

    print(sum)