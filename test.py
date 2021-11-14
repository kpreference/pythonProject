n,m=map(int,input().split())
poke=[]
for i in range(n):
    a=input()
    poke.append(a)
for j in range(m):
    b=input()
    if b.isdigit()==1:
        print(poke[int(b)-1])
    else:
        print(poke.index(str(b))+1)

