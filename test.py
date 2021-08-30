n=int(input())
print(str(bin(n)))
for i in range(2,len(str(bin(n)))):
    print(i)
    print(str(bin(n))[i])
    print()