#20211947 곽선호
b=[12,22,9,9,8,12,2,3,5]
e1=0
e2=0
b.sort()
cnt=0
for i in range(len(b)):

    print(b[i])

    if (e1+b[i])<31:

        e1+=b[i]
        cnt+=1
    elif (e2+b[i])<31:
        e2+=b[i]
        cnt+=1
    else:
        continue

print(e1,e2,cnt)