l=[1,2,3,4,5,1,2,3,4,1,2,3,1,2,1]
d={}
m=0
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
for i in d:
    if i+1 in d and  d[i]+d[i+1]>m:
        m=d[i]+d[i+1]
print(m)