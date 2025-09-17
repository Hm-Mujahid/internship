l=list(map(int,input().split()))
n,m=map(int,input().split())
l2=l[n-1:m:1]
product=1
for i in l2:
    product=product*i
print(product)