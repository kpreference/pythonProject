hy=0
im=0

hh,hm,hs=map(int,input().split(":"))
imh,imm,ims=map(int,input().split(":"))

im+=ims
im+=(imm*60)
im+=(imh*3600)

hy+=hs
hy+=(hm*60)
hy+=(hh*3600)

immm=im-hy
if immm<0:
    immm+=86400

immmm=(immm%3600)

print("%02d:%02d:%02d"%((immm/3600),(immmm/60),(immm%60)))

