n=input()
r=0
for i in range(len(n)):
    if n[i]!=n[len(n)-i-1]:
        r+=1

if r>0:
    print(0)
else:
    print(1)




