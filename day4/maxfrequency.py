#finding max frequency in the hash table
#greedy approach
l=[1,2,3,4,5,1,2,3,4,1,2,3,1,2,1]
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
m=0
ele=0
for i in d:
    if d[i]>m:
        m=d[i]
        ele=i
print(ele,m)