a=int(input())
yee=[1]
yn=0
if a==1:
    yn+=1
    print(1)
else:
    for i in range(1,31):
        yee.append(2*yee[i-1])
        if yee[i]==a:
            print(1)
            yn+=1
            break

if yn==0:
    print(0)