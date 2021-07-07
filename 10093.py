a,b=map(int,input().split())
if b>(a+1):
    print(b - a - 1)
for i in range(a+1,b):
    print(i,end=" ")
