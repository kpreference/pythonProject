a,b,c,d,e,f=map(int,input().split())
ad=a
bd=b
cd=c
da=d
ea=e
fa=f

a=a*d
b=b*d
c=c*d
d=ad*d
e=ad*e
f=ad*f

rx=0
ry=0
ra=0



ry=(c-f)/(b-e)
rx=(cd-(ry*bd))/ad

print("%d %d"%(rx,ry))