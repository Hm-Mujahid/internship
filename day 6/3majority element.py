l=[1,2,3,4,5,1,2,3,4,1,2,3,1,2,1]
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
#find the most frequent value in a list
print(max(d,key=d.get))