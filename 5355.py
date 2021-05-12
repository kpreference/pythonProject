cnt=int(input())


for i in range(cnt):
    a=[]
    #a[0],a[1],a[2],a[3]=input().split(" ")
    a = [i for i in input().split()]


    a[0]=float(a[0])

    for j in range(1,len(a)):
        if a[j]=='@':
            a[0]*=3
        elif a[j]=='%':
            a[0]+=5
        elif a[j]=='#':
            a[0]-=7


    print("%.2f"%a[0])