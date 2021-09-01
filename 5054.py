n=int(input())
for i in range(n):
    dst=0
    nn=int(input())

    nnn=[int(x) for x in input().split()]
    nnn.sort()
    dst=nnn[len(nnn)-1]-nnn[0]
    print(2*dst)