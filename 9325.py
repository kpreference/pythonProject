n=int(input())
for i in range(n):
    cost=int(input())
    m=int(input())
    for j in range(m):
        a,b=map(int,input().split())
        cost+=(a*b)
    print(cost)