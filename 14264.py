import math
n=int(input())

a=math.sqrt(3*n*n)
result=math.sqrt(n*n-a*a/4)
result*=(a/2)
print(result)

