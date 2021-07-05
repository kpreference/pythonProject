a=input()

aa=[]

for i in range(len(a)):
    aa.append(a[i])

aa.sort()
for j in range(len(aa),0,-1):
    print(int(aa[j-1]),end="")
