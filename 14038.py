w=0
for i in range(6):
    a=input()


    if a=='W':
        w+=1


if w>4:
    print(1)
elif w>2:
    print(2)
elif w>0:
    print(3)
else:
    print(-1)
