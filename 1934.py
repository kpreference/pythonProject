#백준 제출 > 시간초과
#아마 for 문으로 돌려서 숫자가 둘다 10000자리 이상일 경우 오래걸리는 것으로 예상
'''
c=int(input())


for i in range(c):
    j=0
    a,b=map(int,input().split())

    if (a==1 and b==1):

        print(a)

    else:

        for j in range(2,a*b+1):

            if ( j%a==0 and j%b==0 ):
                print(j)
                break

'''
''''''
c=int(input())
for i in range(c):
    i=0

    j=0

    cr=0

    s=0

    result=0

    a,b=map(int,input().split())

    if a>b:
        s=b
    else:
        s=a

    for j in range(2,s+1):
        if a%j==0 and b%j==0:
            cr=j
    if cr==0:
        cr=1
    result=(a*b)/cr
    print(int(result))
