'''This script efficiently finds the second-largest number
 in a list by iterating through it only once, 
simultaneously keeping track of both the largest and second-largest values.'''

l=[7,4,5,2,1,6,3]
m1=float('-inf')
m2=float('-inf')
for i in l:
    if i>m1:
        m2=m1
        m1=i
    elif i>m2 and i<m1:
        m2=i
print(m2)
