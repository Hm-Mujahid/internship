from collections import Counter
cheacked_elements = []

l = [1, 5, 3, 3, 3, 5, 2, 5]

# Counter creates a dictionary-like object mapping each element to its count
# For l, this will be: Counter({5: 3, 3: 3, 1: 1, 2: 1})
counts = Counter(l)

for element in l:
    # Check if we have already counted this element
    if element not in checked_elements:
        count = l.count(element)
        # If the count is odd, add it to our result list
        if count % 2 != 0:
            odd_occurrence_elements.append(element)
        # Add the element to our checked list so we don't process it again
        checked_elements.append(element)
print(f"Elements repeated an odd number of times: {odd_occurrence_elements}")