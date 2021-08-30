#a,b,c=map(int,input().split())
a=int(input())
b=int(input())
c=int(input())


result=(a*b*c)
litres=str(result)

reslst=[0 for i in range(10)]

for i in litres:
    reslst[ord(i)-48]+=1
for j in range(10):
    print(reslst[j])