while(1):
    s=input()
    alph=[0 for x in range(26)]
    cnt=0
    if s=='#':
        break
    for i in s:
        if (ord(i)>64 and ord(i)<91) :
            alph[ord(i)-65]+=1
        elif (ord(i)>96 and ord(i)<123):
            alph[ord(i)-97]+=1
    for j in range(26):
        if alph[j]>0:
            cnt+=1
    print(cnt)

