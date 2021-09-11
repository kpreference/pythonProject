em=[0,0,0,0,0,0,0,0]
cnt=0
em[0],em[1],em[2],em[3],em[4],em[5],em[6],em[7]=map(int,input().split())
if em[0]==1:
    cnt=1
    for i in range(8):

        if cnt==em[i]:
            cnt+=1
        else:
            break
    if cnt==9:
        print("ascending")
    else:
        print("mixed")

elif em[0]==8:
    cnt=8
    for i in range(8):
        if cnt==em[i]:
            cnt-=1
        else:
            break
    if cnt==0:
        print("descending")
    else:
        print("mixed")
else:
    print("mixed")

