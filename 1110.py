cnt=0
n=int(input())
a=0
a+=(n%10)*10
a+= ((int(n/10) +  (n%10)) %10)

cnt+=1


while(a!=n):
    b=a
    a = (b % 10) * 10
    a += ((int(b / 10) + (b % 10)) % 10)
    cnt+=1

print(cnt)