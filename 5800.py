n=int(input())
for i in range(n):
    gap=0
    a=[int(x) for x in input().split()]
    nn=a[0]
    del a[0]
    a.sort()
    print("Class %d"%(i+1))
    for j in range(nn-1):
        if gap<(a[j+1]-a[j]):
            gap=a[j+1]-a[j]
    print("Max %d, Min %d, Largest gap %d"%(a[len(a)-1],a[0],gap))