def lcm(a, b):
    return int(a * b / gcd(a, b))
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

a,b=map(int,input().split())
print(gcd(a,b))
