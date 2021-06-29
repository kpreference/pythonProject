n=int(input())
dots=[0,0,0,0,0]
for i in range(n):
    x,y=map(int,input().split())

    if x>0 and y>0:
        dots[1]+=1
    elif x<0 and y>0:
        dots[2]+=1
    elif x<0 and y<0:
        dots[3]+=1
    elif x>0 and y<0:
        dots[4]+=1
    else:
        dots[0]+=1
print("Q1: %d"%dots[1])
print("Q2: %d"%dots[2])
print("Q3: %d"%dots[3])
print("Q4: %d"%dots[4])
print("AXIS: %d"%dots[0])

