word=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
cnt=0
cntw=''
while(1):
   # try:
    a=input()
    for i in a:
        print(i)
        print(ord(i))
        if ord(i)==32 or ord(i)==13:
            pass
        word[ord(i)-97]+=1
    print(word)
  #  except:
   #     break
'''
for j in range(26):
    if word[j] > cnt:
        cnt=word[j]
        cntw=chr(j+97)
    elif word[j] == cnt:
        cntw=cntw+chr(j+97)
        
print(cntw)

'''
#   a  97 z  122