#merging two sorted list in ascenting order in a new list
l2=[2,4,5]
l1=[1,3,6,7,8,9]
res=[]
i,j=0,0
while i<len(l1) and j<len(l2):
    if l1[i]<l2[j]:
        res.append(l1[i])
        i+=1
    else:
        res.append(l2[j])
        j+=1
while i<len(l1):
    res.append(l1[i])
    i+=1
while j<len(l2):
    res.append(l2[j])
    j+=1
print(res)