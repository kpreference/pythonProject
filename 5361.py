n=int(input())
bupu=[350.34,230.90,190.55,125.30,180.90]
for i in range(n):
    sum=0
    a=[int(x) for x in input().split()]
    for j in range(5):
        sum+=(bupu[j]*a[j])

    print("$%.2f"%sum)
