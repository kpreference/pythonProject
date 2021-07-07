cnt=[]
a,b,c=map(int,input().split())
cnt.append(a)
cnt.append(b)
cnt.append(c)
cnt.sort()
for i in range(3):
    print(cnt[i],end=" ")