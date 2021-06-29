n=int(input())
for i in range(n):
    word=[]
    c=0
    a,b=input().split()
    for i in range(0,len(a)):
        ww=ord(b[i]) - ord(a[i])
        if ww<0:
            ww+=26
        word.append(ww)
    print("Distances:",end="")
    for i in range(0,len(word)):
        print(" %d"%word[i],end="")
    print()