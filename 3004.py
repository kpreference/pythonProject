n=int(input())
nn=n
if n%2==1:
    nn+=1
else:
    nn+=2
nn/=2
if n%2==1:
    print(int(nn*(nn+1)))
else:
    print(int(nn*nn))
