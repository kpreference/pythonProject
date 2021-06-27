n=int(input())
cute=[0,0]
for i in range(n):
    a=int(input())
    cute[a]+=1
if cute[0]>cute[1]:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")