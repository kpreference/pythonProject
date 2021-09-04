s=input()
# a 97 z 122
# A 65 Z 90
for i in s:
    if ord(i)>64 and ord(i)<91:
        if (ord(i)+13)>90:
            print(chr(ord(i)-13),end="")
        else:
            print(chr(ord(i)+13),end="")

    elif ord(i)>96 and ord(i)<123:
        if (ord(i)+13)>122:
            print(chr(ord(i)-13),end="")
        else:
            print(chr(ord(i)+13),end="")
    else:
        print(i,end="")