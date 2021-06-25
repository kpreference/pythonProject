a,b=map(int,input().split())
ar=0
br=0
ar+=(a//100)
a-=(ar*100)
ar+=((a//10)*10)
ar+=((a%10)*100)

br+=(b//100)
b-=(br*100)
br+=((b//10)*10)
br+=((b%10)*100)
if ar<br:
    print(br)
else:
    print(ar)
