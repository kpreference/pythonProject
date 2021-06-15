# n=int(input())
# aver=0
# peo=0
# for i in range(n):
#
#     qldbf=0
#
#     aaa=0
#
#     score = [int(x) for x in input().split()]
#
#     for j in range(1,score[0]+1):
#         aver+=score[j]
#        # print(aver)
#     j=0
#
#     print(aver)
#     for j in range(1,score[0]+1):
#
#         if (aver/score[0])<score[j]:
#
#             peo+=1
#
#
#     qldbf=100*(peo/score[0])
#
#     print("%.3f%%" %qldbf)
#
#     aver=0
#     j=0
#     peo=0
#     score=[0,]

#하다가 안돼서종호가 풀어줌
c = int(input())
for i in range(c):
    total = 0
    userInput = [int(x) for x in input().split()]
    for j in range(userInput[0]):
        total += userInput[j+1]
    average = total / userInput[0]
    count = 0
    for j in range(userInput[0]):
        if userInput[j+1] > average:
            count+=1
    result=100*(count/userInput[0])
    print("%.3f%%" %result )
