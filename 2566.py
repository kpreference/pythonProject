num=[]
for k in range(9):
    a=[int(x) for x in input().split()]
    num.append(a)
cnt=0
cnti=0
cntj=0
for i in range(9):
    for j in range(9):
        if num[i][j]>cnt:
            cnt=num[i][j]
            cnti=i
            cntj=j
print(cnt)
print(cnti+1,cntj+1)