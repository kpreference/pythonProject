import math as m
d,h,w=map(int,input().split())
sum=((h*h)+(w*w))**(1/2)
hh=(d/sum*h)
ww=(d/sum*w)

print(int(hh),int(ww))
