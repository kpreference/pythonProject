n=int(input())
i=2
while 1:
    if n==1:
        break
    elif n%i==0:
        print(i)
        n=n/i
        if n == 1:
            break
    else:
        i+=1
