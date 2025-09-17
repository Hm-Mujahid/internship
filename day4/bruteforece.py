#This script finds the second-largest number in a list by first finding the largest number,
#  and then looping through the list a second time to find the 
# largest number that is smaller than the first one.

l=[7,4,5,2,1,6,3]
m1=float('-inf')
m2=float('-inf')
for i in l:
    if i>m1:
        m1=i
for i in l:
    if i>m2 and i<m1:
        m2=i
print(m2)
    
