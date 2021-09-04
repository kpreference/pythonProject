n=int(input())
su=[]
for i in range(n):
    w=int(input())
    su.append(w)
if (su[1]-su[0])==(su[2]-su[1]):

    print(su[len(su)-1]+(su[1]-su[0]))
elif (su[1]/su[0])==(su[2]/su[1]):
    print("%d"%(su[len(su) - 1] * (su[1] / su[0])))
