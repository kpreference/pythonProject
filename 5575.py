def toi(x1,x2,x3,x4,x5,x6):
    sum=0
    sum2=0
    sum+=x3
    sum+=x2*60
    sum+=x1*3600

    sum2+=x6
    sum2+=x5*60
    sum2+=x4*3600

    sum2-=sum
    summ=(sum2%3600)
    print(int(sum2/3600),int(summ/60),sum2%60)

a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
c=[int(x) for x in input().split()]
toi(a[0],a[1],a[2],a[3],a[4],a[5])
toi(b[0],b[1],b[2],b[3],b[4],b[5])
toi(c[0],c[1],c[2],c[3],c[4],c[5])

