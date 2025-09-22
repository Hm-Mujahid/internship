l=[3,2,3,2,3,3,3,3,2,2,2,3,3]
'''moorse voting algorithm
1. Initialize a candidate element and a count variable.
2. Iterate through the list of elements.
3. If the count is zero, set the current element as the candidate and set count to 1.
4. If the current element is the same as the candidate, increment the count.
5. If the current element is different from the candidate, decrement the count.
6. After one pass through the list, the candidate will be the majority element.'''
candidate = l[0]
vote = 0
for i in l:
    if vote == 0:
        candidate = i
    elif candidate == i:
        vote += 1
    else:
        vote -= 1
print(candidate)