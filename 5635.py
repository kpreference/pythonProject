n=int(input())

sname=""
sdd=0
smm=0
syyyy=0

dname=""
ddd=0
dmm=0
dyyyy=2011

for i in range(n):
    name,dd,mm,yyyy=input().split()
    dd=int(dd)
    mm=int(mm)
    yyyy=int(yyyy)

    if yyyy == syyyy:
        if mm > smm:
            sname = name
            sdd = dd
            smm = mm
            syyyy = yyyy
        elif mm == smm:
            if dd > sdd:
                sname = name
                sdd = dd
                smm = mm
                syyyy = yyyy

    elif yyyy>syyyy:
        sname=name
        sdd=dd
        smm=mm
        syyyy=yyyy

    if yyyy == dyyyy:
        if mm < dmm:
            dname = name
            ddd = dd
            dmm = mm
            dyyyy = yyyy
        elif mm == dmm:
            if dd < ddd:
                dname = name
                ddd = dd
                dmm = mm
                dyyyy = yyyy
    elif yyyy<dyyyy:
        dname = name
        ddd = dd
        dmm = mm
        dyyyy = yyyy



print(sname)

print(dname)
