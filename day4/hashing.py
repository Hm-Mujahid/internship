#numer of time a value is ocuuring in a list
#hasing - frequency table for a given list of finte and small values
#hashing is very easy to implement using dictionary in python
l=[1,2,3,4,5,1,2,3,4,1,2,3,1,2,1]
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)