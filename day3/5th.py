l=[1,5,7,4,8,2]
sum=0
for i in range(len(l)):
    if i%2==0 and l[i]%2==0:
        sum +=l[i]
print(sum)