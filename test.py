n=int(input())
q=[]
for i in range(n):
    a=input()
    if a[0:4]=="push":
        q.append(int(a[5:]))
    elif a=="pop":
        if len(q)>0:
            print(q[0])
            q.pop(0)
        else:
            print(-1)
    elif a=="size":
        print(len(q))
    elif a=="empty":
        if len(q)==0:
            print(1)
        else:
            print(0)
    elif a=="front":
        if len(q)==0:
            print(-1)
        else:
            print(q[0])
    elif a=="back":
        if len(q)==0:
            print(-1)
        else:
            print(q[len(q)-1])




    #확인
    #print(q)

