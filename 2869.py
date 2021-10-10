a,b,v=map(int,input().split())
cnt=0
v-=a
cnt+=1

if v>0:
    if v%(b-a)==0:
        cnt+=int(v/(a-b))
    else:
        cnt += int(v / (a - b))
        cnt+=1
print(cnt)