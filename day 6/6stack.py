s = "{[()]}"
stack = []

for c in s:
    if c in "(":
        stack.append(")")
    elif c in "[":
        stack.append("]")
    elif c in "{":
        stack.append("}")
    elif not stack or stack.pop() != c:
        print(False)
        break
print(len(stack) == 0)