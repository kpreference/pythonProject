n=int(input())
for i in range(n):
    a=input()
    mo = 0
    ja = 0
    for j in a:

        if j=="a" or j=="e" or j=="o" or j=="i" or j=="u" or j=="A" or j=="E" or j=="I" or j=="O" or j=="U":
            mo+=1
        elif j==" ":
            pass
        else:
            ja+=1
    print(ja,mo)