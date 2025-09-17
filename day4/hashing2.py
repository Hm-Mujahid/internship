#hashing without using dictionary
l=[1,2,3,4,5,1,2,3,4,1,2,3,1,2,1]
res=[0]*len(l)
for i in range(len(l)):
    if l[i] not in res:
        res[i]=1
    else:
        res[i]+=1
print(res)

        