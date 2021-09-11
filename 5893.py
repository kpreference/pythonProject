n=int(input(),2)
for i in range(2,len(str(bin(int(n)*17)))):
    print(str(bin(int(n)*17))[i],end="")