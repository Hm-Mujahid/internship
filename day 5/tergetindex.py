numbers=[2,7,11,15]
target=9

for i in range(len(numbers)):
     for j in range(i+1,len(numbers)):
         if (numbers[i]+numbers[j]==target):
                print([i,j])
                break
         
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i,j=0,len(nums)-1
        res=[-1,-1]
        while i<j:
            if nums[i]+nums[j]==target:
                return[i+1,j+1]
            elif(nums[i]+nums[j])>target:
                j-=1
            else:
                i+=1'''