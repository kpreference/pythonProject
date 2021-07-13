def pan(dice):
    cnt=0
    if dice[0]==dice[1] and dice[1]==dice[2] and dice[2] == dice[3]:
        return 1
    elif  ( dice[0]==dice[1] and dice[1]==dice[2] ) or ( dice[0]==dice[1] and dice[1]==dice[3] ) or ( dice[0]==dice[3] and dice[2]==dice[3] ) or ( dice[3]==dice[1] and dice[1]==dice[2] ) :
        return 2
    elif ( dice[0]==dice[1] and dice[2]==dice[3] ) or ( dice[0]==dice[2] and dice[1]==dice[3] ) or ( dice[0]==dice[3] and dice[1]==dice[2] ) :
        return 3
    elif  dice[0]==dice[1] or dice[1]==dice[2] or dice[2]==dice[3] or dice[1]==dice[3] or dice[0]==dice[2] or dice[0]==dice[3] :
        return 4
    else :
        return 5
n=int(input())
result=0
for i in range(n):
    gain = 0
    dice=[int(x) for x in input().split()]
    dice.sort()
    tr=0
    if pan(dice)==1:
        gain+=50000
        gain+=(dice[1]*5000)
    elif pan(dice)==2:
        gain+=10000
        gain+=(dice[1]*1000)
    elif pan(dice) == 3:
        gain += 2000
        gain += (dice[1] * 500)
        gain += (dice[2]*500)
    elif pan(dice)==4:
        if dice[0]==dice[1] :
            tr=dice[0]
        elif dice[1] == dice[2] :
            tr=dice[1]
        elif dice[2] == dice[3]:
            tr=dice[2]
        gain+=1000
        gain+=(tr*100)
    elif pan(dice)==5:
        j=0
        tr=dice[0]
        for j in range(1,4):
            if dice[j]>tr:
                tr=dice[j]
        gain=(tr*100)
    if gain>result:
        result=gain
print(result)

