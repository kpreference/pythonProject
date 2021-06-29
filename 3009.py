xx=[]
yy=[]
xr=0
yr=0

for i in range(3):
    x,y=map(int,input().split())
    xx.append(x)
    yy.append(y)


xx.sort()
yy.sort()

if xx[1]==xx[0]:
    xr=xx[2]
elif xx[1]==xx[2]:
    xr=xx[0]

if yy[1]==yy[0]:
    yr=yy[2]
elif yy[1]==yy[2]:
    yr=yy[0]

print(xr,yr)