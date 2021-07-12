n=int(input())
for i in range(n):
    sum=0
    a=int(input())
    for j in range(1,a+1,2):
        sum+=j
    print(sum)
    j=0