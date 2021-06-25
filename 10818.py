n=int(input())
x=[int(i) for i in input().split()]
x.sort()
print("%d %d"%(x[0],x[n-1]))
