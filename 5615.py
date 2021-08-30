def area(x):
    res=0
    for i in range(1,x+1):
        for j in range(1,x+1):
            if (2*i*j+i+j)==x:
                res+=1
                break

    if res>1:
        return 1
    else:
        return 0




n=int(input())
sum=0
for i in range(n):
    a=int(input())
    sum+=area(a)
print(sum)