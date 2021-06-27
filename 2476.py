n=int(input())

result=0
big=0
for i in range(n):
    a, b, c = map(int, input().split())
    sum = 0
    if a==b and b==c and c==a :
        sum+=10000
        sum+=(a*1000)
    elif a==b and b!=c:
        sum+=1000
        sum+=(a*100)
    elif c == b and b != a:
        sum += 1000
        sum += (b * 100)
    elif a == c and c != b:
        sum += 1000
        sum += (a * 100)
    else:
        big=a
        if big<b:
            big=b
        if big<c:
            big=c
        sum+=(big*100)
    if sum>result:
        result=sum
print(result)