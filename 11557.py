n=int(input())

for i in range(n):
    m=int(input())
    school_lst=[]
    pan=0
    sc_pan=""
    for j in range(m):
        sc,ca=input().split() #school count_alch
        school_lst.append(sc)
        school_lst.append(int(ca))
    for k in range(1,len(school_lst),2):
        if pan<school_lst[k]:
            pan=school_lst[k]
            sc_pan=school_lst[k-1]


    print(sc_pan)


