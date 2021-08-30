yori=[0,0,0,0,0]

for i in range(5):
    a,b,c,d=map(int,input().split())

    yori[i] +=a
    yori[i] +=b
    yori[i] +=c
    yori[i] +=d

bstsc=0
bstco=0

for j in range(5):
    if yori[j]>bstsc:
        bstsc=yori[j]
        bstco=(j+1)

print(bstco,bstsc)