n=input()

for i in n:
    if i.isupper()==True:
        print(i.lower(),end="")
    else:
        print(i.upper(),end="")