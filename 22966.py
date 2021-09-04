n=int(input())
book=[]
nan=5
nanm=0
for i in range(n):
    a,b=input().split()
    book.append(a)
    book.append(b)

for j in range(1,len(book),2):
    if int(book[j])<nan:
        nan=int(book[j])
        nanm=j-1
print(book[nanm])
