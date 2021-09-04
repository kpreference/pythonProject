def ccc(x):
    cnt=0
    for i in str(x):
        if i=='0':
            cnt+=1
    return cnt

cnnt=0
n=int(input())

for i in range(n):
    cnnt=0
    a,b=map(int,input().split())
    for j in range(a,b+1):
        cnnt+=ccc(j)
    print(cnnt)