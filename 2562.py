arr=[]
b=0
bc=0

for i in range(1,10):
    n=int(input())
    arr.append(n)
    if arr[i-1]>b:
        b=arr[i-1]
        bc=i
print(b)
print(bc)
