def rev(x):
    result=0
    result+=((x%10)*100)
    result+=int(x/100)
    x-=(x%10)
    x-=(int(x/100)*100)
    result+=x
    return result

xx,y=map(int,input().split())
print(rev(xx),rev(y))
print(rev(rev(xx)+rev(y)))
