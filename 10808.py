s=input()

ss=[0 for x in range(26)]

for i in s:
    ss[ord(i)-97]+=1
for j in range(26):
    print("%d"%ss[j],end=" ")
