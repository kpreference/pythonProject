n=input()
tot=10
for i in range(1,len(n)):
    if n[i]==n[i-1]:
        tot+=5
    else:
        tot+=10
print(tot)