while(1):
    a=input()
    if int(a)==0:
        break
    aa=len(a)

    cnt=0

    if aa%2==1:
        for i in range(0,aa):
            if a[i] != a[aa-i-1]:
                cnt+=1

    else:
        for i in range(aa):
            if a[i] != a[aa - i-1]:
                cnt+=1


    if cnt>0:
        print("no")
    else:
        print("yes")