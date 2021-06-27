def rev(x):
    result = 0
    if x==1000 or x==100 or x==10 or x==1:
        return 1
    elif x>100:
        result+=(x//100)

        x-=(result*100)

        result+=(x%10)*100

        result+=(x//10)*10

        return result

    elif x>10:
        result+=((x%10)*10)
        result+=(x//10)

        return result
    elif x<10:
        return x*100


a,b=map(int,input().split())


print(rev(rev(a)+rev(b)))
