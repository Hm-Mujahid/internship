#finding 2nd max frequency in the hash table
#brute force approach
l=[2,3,4,5,1,2,3,4,1,2,3,1,2,1,2]
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
m1,m2=0,0
ele1,ele2=0,0
for i in d:
    if d[i]>m1:
        m2=m1
        m1=d[i]
        ele2=ele1
        m1=d[i]
        ele=i
for i in d:
    if d[i]>m2 and d[i]!=m1:
        m2=d[i]
        ele2=i
print(ele2)
    