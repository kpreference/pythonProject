inp=input()

wrd=[]
cnt=[]


for i in inp:

    if ord(i)>96 and ord(i)<123:

        if wrd.find(chr(ord(i)-32) == -1 :
            wrd.append(chr(ord(i) - 32))
            cnt[wrd.find(chr(ord(i) - 32)]+=1

        else:

            cnt[wrd.find(chr(ord(i) - 32)] += 1


    elif ord(i)>64 and ord(i)<91:
        if wrd.find(chr(ord(i)) != -1:
            wrd.append(chr(ord(i)))
        cnt[wrd.find(chr(ord(i))] += 1

        else:
        cnt[wrd.find(chr(ord(i))] += 1
cnt.sort()
print(cnt[0])



#AZaz 65 90 97 122