def fun(energy,idx):
    if idx==0:
        return 0
    jump1=fun(energy,idx-1)+abs(energy[idx]-energy[idx-1])
    jump2=float('inf')#infinity initialization
    if idx>1:
        jump2=fun(energy,idx-2)+abs(energy[idx]-energy[idx-2])
    return min(jump1,jump2)
energy=[10,30,40,20]
n=len(energy)-1
print(fun(energy,n))
