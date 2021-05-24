sum=0
s=int(input())
sum=s
if s==1:
    print(1)
else:
    for i in range(1,s):
        sum-=i
        if i>=sum:
            print(i)
            break
