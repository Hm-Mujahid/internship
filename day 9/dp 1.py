#write the problem in terms of indexes
#do all the operations given in the q for that index
#if question says find all posiible sol then add eventing
   #min-find min    max-find max
def dp(n):

        prev1 = 3
        prev2 = 2
        cur = 0

        for _ in range(3, n):
            cur = prev1 + prev2
            prev2 = prev1
            prev1 = cur
        
        return cur
n=int(input())
print(dp(n))