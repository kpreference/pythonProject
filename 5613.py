result=int(input())
while(1):
    a=input()
    if a=='+':
        result+=int(input())
    elif a=='-':
        result-=int(input())

    elif a=='*':
        result*=int(input())
    elif a=='/':
        result/=int(input())
        result=int(result)
    else:
        break
print(result)