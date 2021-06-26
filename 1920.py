n=int(input())
nn=[int(i) for i in input().split()]
m=int(input())
mm=[int(j) for j in input().split()]

i=0
j=0

for i in range(m):
    tf=0
    for j in range(n):
        if mm[i]==nn[j]:
            tf+=1
    if tf>0:
        print(1)
    else:
        print(0)