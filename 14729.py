n=int(input())
a=[]
for i in range(n):
    aa=float(input())
    a.append(aa)
a.sort()
for i in range(0,7):
    print("%.3f"%a[i])
