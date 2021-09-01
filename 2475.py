sum=0
a,b,c,d,e=map(int,input().split())
sum+=(a*a)
sum+=(b*b)
sum+=(c*c)
sum+=(d*d)
sum+=(e*e)
print(sum%10)