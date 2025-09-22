sandwichs=[0,1,0,1]
students=[1,1,0,0]
n=len(students)
while students and sandwichs and sandwichs[0] in students and n!=0:
    if students[0]==sandwichs[0]:#list[0] gives first top of queue
        students.pop(0)
        sandwichs.pop(0)
        n-=1
    else:
        students.append(students.pop(0))
print(len(students))