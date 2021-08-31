n=int(input())
sc=[int(x) for x in input().split()]
sc.sort()
ms=sc[len(sc)-1]

sum=0

for i in range(len(sc)):
    sc[i]=(sc[i]/ms*100)
    sum+=sc[i]

print(sum/n)