n=int(input())
cnt=0
a=[int(x) for x in input().split()]

for i in range(5):
    if a[i]==n:
        cnt+=1
print(cnt)