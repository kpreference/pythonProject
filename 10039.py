sc=[0,0,0,0,0]
sum=0
for i in range(5):
    sc[i]=int(input())
    if sc[i]<40:
        sc[i]=40
    sum+=sc[i]

print(int(sum/5))