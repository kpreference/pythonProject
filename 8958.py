n=int(input())

for i in range(n):
    a=input()
    score=0
    ox=1
    for j in a:
        if j=="O":
            score+=ox
            ox+=1
        elif j=="X":
            ox=1
    print("%d"%score)