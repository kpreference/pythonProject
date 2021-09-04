a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())

sc=[]
sc.append(a)
sc.append(b)
sc.append(c)
sc.append(d)

so=[]
so.append(e)
so.append(f)

sc.sort()
so.sort()
sum=0
for i in range(1,4):
    sum+=sc[i]

print(sum+so[1])