'''
Given an integer array nums, Find the subarray with tha largest sum and return its sum 
'''

nums = [5,4,-1,7,8]

cur = nums[0]
res= nums[0]

for i in range(1,len(nums)):
    cur = max(nums[i],nums[i]+cur)
    res = max(cur,res)

print(res)
