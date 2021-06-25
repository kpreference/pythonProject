n=input()
word=[]
for j in range(26):
    word.append(-1)

for i in range(len(n)):
    if (word[ord(n[i])-97])==(-1):
        word[ord(n[i])-97] = i
j=0
for j in range(26):
    print(word[j],end=" ")