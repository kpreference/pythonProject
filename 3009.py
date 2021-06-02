dox=[]
doy=[]

x=0
y=0

for i in range(3):
    a,b=map(int,input().split())
    dox.append(a)
    doy.append(b)

dox.sort()
doy.sort()

if dox[0]==dox[1]:
    x=dox[2]
elif dox[2]==dox[1]:
    x=dox[0]
if doy[0]==dox[1]:
    y=doy[2]
elif doy[2]==doy[1]:
    y=doy[0]

print("%d %d"%(x,y))

#뭐가문제지