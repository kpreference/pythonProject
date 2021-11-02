i=1
j=1
while(1):
    print("%d * %d = %d"%(i,j,i*j))
    if j==9:
        j=1
        i+=1
        print()
    j+=1
    if i==9 and j==9:
        break