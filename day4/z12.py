n=int(input())
vote=list(map(int,input().split()))
age=list(map(int,input().split()))
d={}
for i in range(n):
    if age[i] not in d:
        d[vote[i]]=1
    else:
        d[vote[i]]+=1
print(d)