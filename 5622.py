#틀림


n=input()
#A Z 65 90
sum=0
for i in n:
    if ord(i)>64 and ord(i)<68: #abc
        sum+=2
    elif ord(i) > 67 and ord(i) < 71: #def
        sum+=3
    elif ord(i) > 70 and ord(i) < 74: #ghi
        sum +=4
    elif ord(i) > 73 and ord(i) < 77: #jkl
        sum +=5
    elif ord(i) > 76 and ord(i) < 80: #mno
        sum +=6
    elif ord(i) > 79 and ord(i) < 84: #pqrs
        sum +=7
    elif ord(i) > 83 and ord(i) < 87: #tuv
        sum +=8
    elif ord(i) > 86 and ord(i) < 91: #WXYZ
        sum +=9
print(sum+2)