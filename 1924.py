a,b=map(int,input().split())

week=['SUN','MON','TUE','WED','THU','FRI','SAT']

month=[31,28,31,30,31,30,31,31,30,31,30,31]

date=0


for i in range(a-1):
    date+=month[i]

date+=b

print(week[date%7])