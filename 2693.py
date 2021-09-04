n=int(input())
for i in range(n):
    a=[int(x) for x in input().split()]
    a.sort()
    print(a[len(a)-3])