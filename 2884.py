h,m=map(int,input().split())
tot_m=(h*60+m)

if tot_m<45:
    tot_m+=1440
elif tot_m>1440:
    tot_m-=1440
tot_m-=45
h=tot_m//60
m=tot_m%60
print(h,m)