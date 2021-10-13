a=[]
n=int(input())
for i in range(n):
    aa=[int(x) for x in input().split()]
    for j in range(n):
        a.append(aa[j])
a.sort()
print(a)
print(a[len(a)-n])