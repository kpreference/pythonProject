n=int(input())
for i in range(n):
    a,b=map(int,input().split())

    print("You get %d piece(s) and your dad gets %d piece(s)."%(a/b,a%b))