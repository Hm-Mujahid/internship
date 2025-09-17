def check_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True     
l=[60,2,10,30,7,40,90,50,70]
count=0
for i in l:
    if check_prime(i):
        count+=1
print(count)