n=[]

for i in range(10):
    cnt=0
    a=int(input())
    for j in range(len(n)):
        if n[j]==(a%42):
            cnt+=1
    if cnt==0:
        n.append((a%42))

print(len(n))

