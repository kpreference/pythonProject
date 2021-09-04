while True:
    try:
        sm=0
        dm=0
        sj=0
        gb=0
        a=input()
        for i in a:
            if ord(i)==32:
                gb+=1
            elif ord(i)>47 and ord(i)<58:
                sj+=1
            elif ord(i)>96 and ord(i)<123:
                sm+=1
            elif ord(i) > 64 and ord(i) < 91:
                dm+=1
        print(sm,dm,sj,gb)
    except:
        break