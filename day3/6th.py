# to take only unique values from a list

# Original list with duplicate values
original_list = [1, 2, 2, 3, 4, 4, 4, 5, 1]

# To get unique values, we can convert the list to a set.
# A set is a data structure that only stores unique elements.
unique_set = set(original_list)

# If you need the result as a list again, you can convert it back.
unique_list = list(unique_set)

print(f"Original list: {original_list}")
print(f"List with unique values: {unique_list}")