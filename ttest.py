#20211947 곽선호
b=[2,3,5,8,9,9,12,12,22]
e1=[0]
e2=[0]
cnt=0
b.sort()
for i in range(len(b)):
    if sum(e1) < 30:
        if (sum(e1)+b[i]) > 30 :
            if (sum(e1)-e1[len(e1)-1] + b[i]) < 31:
                e1.pop()
                e1.append(b[i])
        else:
            e1.append(b[i])
            cnt+=1
e1.pop(0)
for j in range(0,len(e1)):
    for k in range(0,len(b)):
        if e1[j] == b[k]:
            b.pop(k)
            #print(e1,b)
            break
for i in range(len(b)):
    if sum(e2) <= 30:
        if (sum(e2)+b[i]) > 30 :
            if sum(e2)-e2[len(e2)-1] + b[i] <31:
                e2.pop()
                e2.append(b[i])
        else:
            e2.append(b[i])
            cnt+=1
e2.pop(0)
print(e1,e2)
print(cnt)
