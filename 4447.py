n=int(input())
for i in range(n):
    g=0
    b=0
    a=''
    a=input()
    for j in a:
        if ord(j)==66 or ord(j)==98:
            b+=1
        elif ord(j)==71 or ord(j)==103:
            g+=1

    if b>g:
        print("%s is A BADDY"%a)
    elif b<g:
        print("%s is GOOD" % a)
    else:
        print("%s is NEUTRAL" % a)