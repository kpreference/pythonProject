b=int(input())
kPa=(b*5-400)
print(kPa)
result=0
if b<kPa:
    result-=1
elif b>kPa:
    result+=1
print(result)