import math
t=int(input())
for i in range(t):
    h,w,n=map(int,input().split())

    if n%h==0:
        print(h,end="")
    else:
        print(n%h,end="")
    print("%02d"%math.ceil(n/h))
    '''
        if n%h==0:
            print(h,end="")
            if (int(n / h) + 1) < 10:
                print(str(0) + str((int(n / h) )))
            else:
                print(str((int(n / h) )))
        else:
            print(n%h,end="")
            if (int(n / h) + 1) < 10:
                print(str(0) + str((int(n / h) + 1)))
            else:
                print(str((int(n / h) + 1)))

    '''