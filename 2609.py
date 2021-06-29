def lcd(a, b):
    return int(a * b / gcd(a, b))
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a


result=1
a,b=map(int,input().split())
print(gcd(a,b))
print(lcd(a,b))
#유클리드호제법