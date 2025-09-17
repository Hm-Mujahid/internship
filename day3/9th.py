l=[60,80,10,30,20,40,90,50,70]
n=45
m=75
res=[]
for i in l:
    if i in range(n,m):
        res.append(i)
print(res)
res2=1
for i in res:
    res2=res2*i
print(res2)