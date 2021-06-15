n=int(input())

a1=0
a2=1
a3=1

for i in range(n-1):
    a3=a1+a2
    a1=a2
    a2=a3
if n==0:
    print(0)
elif n<=20:
    print(a3)
else:
    pass

