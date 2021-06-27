n=int(input())
p=input()

ab=[0,0]

for i in p:
    if i=='A':
        ab[0]+=1
    elif i=='B':
        ab[1]+=1

if ab[0]==ab[1]:
    print("Tie")
elif ab[0]>ab[1]:
    print("A")
elif ab[0]<ab[1]:
    print("B")
