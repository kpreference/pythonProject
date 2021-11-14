def ba5(x):
    if x%125==0:
        return 3
    elif x%25==0:
        return 2
    elif x%5==0:
        return 1
fac=1
n=int(input())
cnt=0
for i in range(5,n+1,5):
    cnt+=ba5(i)

print(cnt)