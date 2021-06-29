n=int(input())
for i in range(n):
    ab=[]

    c=0
    a,b=map(int,input().split())
    if a > b:   # b>a
        c = b
        b = a
        a = c

    if a%b==0 or b%a==0:
        print(b)
    else:
        c=1
        while(1):

            for j in range(2,b+1):
                if a%j==0 and b%j==0 :
                    ab.append(j)
                    a//=j
                    b//=j
                    break
            if j==b:
                ab.append(a)
                ab.append(b)
                break
        for k in range(len(ab)):
            c*=ab[k]
        print(c)






