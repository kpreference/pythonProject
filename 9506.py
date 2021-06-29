while(1):
    n_lst=[]

    n=int(input())

    if n==(-1):
        break

    for i in range(1,n):
        if n%i==0:
            n_lst.append(i)

    if n==sum(n_lst):
        print("%d = %d"%(n,n_lst[0]),end="")

        for k in range(1,len(n_lst)):
            print(" + %d"%(n_lst[k]),end="")

    else:
        print("%d is NOT perfect."%n,end="")

    print()