nums1=[4,2,3,1]
nums2=[2,4,6,8,10]
res=[]
for i,j in range(len(nums1)),nums2:
   
    if nums1[i]<j:
        res.append(j)
    else:
        res.append(-1)
print(res)
