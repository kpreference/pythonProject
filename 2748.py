n=int(input())
n1=0
n2=1
sum=0
if n!=1:

    for i in range(n-1):
        sum=n1+n2
        n1=n2
        n2=sum
else:
    sum+=1
print(sum)