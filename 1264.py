while(1):
    sum=0
    a=input()
    if a=='#':
        break
    for i in a:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='O' or i=='I' or i=='U':
            sum+=1
    print(sum)