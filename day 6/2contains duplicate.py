l=[1,2,3,4]
s=set()#empty set
for i in l:
    if i not  in s:
        s.add(i)
    else:
        print(True)
        break
print(False)