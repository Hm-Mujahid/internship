energy=[30,10,60,10,60,50]
n=len(energy)
dp=[0]*n
if n>1:
    dp[1]=abs(energy[1]-energy[0])
for i in range(2,n):
    dp[i]=min(dp[i-1]+abs(energy[i]-energy[i-1]),dp[i-2]+abs(energy[i]-energy[i-2]))
print(dp[n-1])