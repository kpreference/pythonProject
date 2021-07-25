n=int(input())
for i in range(n):
     cnt=0
     a=input()

     for j in a:
          if cnt==0:
               cd=ord(j)
               if cd>96 and cd<123:

                    print(chr(cd-32),end="")
               else:

                    print(j,end="")

               cnt += 1

          else:
               print(j,end="")
     print()