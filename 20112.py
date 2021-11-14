n=int(input())
a=[]
for i in range(n):
    nn=input()
    a.append(nn)
cnt=0
for i in range(0,n):
    for j in range(0,n):
        if a[i][j]!=a[j][i]:
            cnt+=1
if cnt==0:
    print("YES")
else:
    print("NO")
