l=[1,5,7,4,8,2]
l2=l[1:7:2]
sum=0
for i in l2:
    if i%2==0:
        sum +=i
print(sum)
print(l2)