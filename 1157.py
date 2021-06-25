n=input()

bst=0
bstn=0
al=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in n:
    if ord(i)>64 and ord(i)<91:
        al[ord(i)-65]+=1
    elif ord(i)>96 and ord(i)<123:
        al[ord(i) - 97] += 1
p=0
for j in range(0,26):
    p=0
    if al[j]!=0 and al[j]==bst:
        for k in range(j,26):
            if al[j]<al[k]:
                p+=1
        if p==0:
            print("?")
            break
    elif al[j]>bst:
        bst=al[j]
        bstn=j
if j==25:
    print(chr(bstn+65))
