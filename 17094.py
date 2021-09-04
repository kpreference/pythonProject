n=int(input())
s=input()

cnt2=0

cnte=0

for i in s:
    if i=='2':
        cnt2+=1
    elif i=='e':
        cnte+=1

if cnte==cnt2:
    print("yee")
elif cnte>cnt2:
    print("e")
elif cnt2>cnte:
    print("2")