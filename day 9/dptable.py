def fun(energy,idx,dp):
    if idx==0:
        return 0
    jump1=fun(energy,idx-1,dp)+abs(energy[idx]-energy[idx-1])
    jump2=float('inf')#infinity initialization
    if idx>1:
        jump2=fun(energy,idx-2,dp)+abs(energy[idx]-energy[idx-2])
    dp[idx]=min(jump1,jump2)
    return dp[idx]
energy=[10,30,40,20]
n=len(energy)-1
dp=[-1]*(n+1)
print(fun(energy,n,dp))
