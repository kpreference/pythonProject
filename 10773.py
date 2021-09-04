n=int(input())
a=[]
for i in range(n):
    nn=int(input())
    if nn==0:
        del a[len(a)-1]
    else:
        a.append(nn)
print(sum(a))