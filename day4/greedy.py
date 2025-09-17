'''This script finds the largest number in a list by checking each element
 one by one and keeping track of the biggest value it has found so far.'''

l=[7,4,5,2,1,6,3]
m=float('-inf')
for i in l:
    if i>m:
        m=i
print(m)
