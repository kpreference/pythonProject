a,b,c=map(int,input().split())

sum=0

cc=0

if a==b==c :
    sum+=10000
    sum+=(a*1000)
elif a==b or a==c or b==c :
    sum+=1000
    cc=a
    if a<b:
        b=cc
    if cc<c:
        cc=c
    sum+=(cc*100)
else:
    cc = a
    if a < b:
        b = cc
    if cc < c:
        cc = c
    sum += (cc * 100)
print(sum)