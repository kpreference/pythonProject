def lcd(a, b):
    return int(a * b / gcd(a, b))
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
n=int(input())
for i in range(n):
    c=0
    result=1
    a,b=map(int,input().split())
    print(lcd(a,b))
