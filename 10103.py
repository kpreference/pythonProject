n=int(input())
ascore=100
bscore=100
for i in range(n):
    a,b=map(int,input().split())
    if a==b:
        pass
    elif a>b:
        bscore-=a
    elif a<b:
        ascore-=b

print(ascore)
print(bscore)