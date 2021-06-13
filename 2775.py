def people_count(k,n):
    global cnt
    i=0
    if k==0:
        cnt+=n
    else:
        m=0
        for m in range(k):
            for p in range(k):
                people_count(m,p)

    return cnt

a=int(input())

for j in range(a):
    global cnt
    cnt=0
    k = int(input())
    n = int(input())

    print(people_count(k,n))


