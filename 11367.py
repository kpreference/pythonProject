n=int(input())
for i in range(n):
    name,sc=input().split()
    grade=''
    score=int(sc)
    if score>96:
        grade='A+'
    elif score>89:
        grade = 'A'
    elif score>86:
        grade = 'B+'
    elif score>79:
        grade = 'B'
    elif score>76:
        grade = 'C+'
    elif score>69:
        grade = 'C'
    elif score>66:
        grade = 'D+'
    elif score>59:
        grade = 'D'
    else:
        grade='F'
    print(name,grade)

