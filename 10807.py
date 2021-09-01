n=int(input())
nn=[int(x) for x in input().split()]
nnn=int(input())
cnt=0
for i in range(n):
    if nn[i]==nnn:
        cnt+=1
print(cnt)