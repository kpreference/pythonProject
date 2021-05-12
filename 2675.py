t=int(input())
for i in range(t):
    r,s = input().split(" ")
    for j in range(len(s)):
        for k in range(int(r)):
            print(s[int(j)],end="")


    print()