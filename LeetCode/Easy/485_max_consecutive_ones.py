class Solution:
    def findMaxConsecutiveOnes(self, nums):
      one=0
      mx=0
      for i in range(len(nums)):
        if nums[i]==1:
          one+=1
        else:
          one=0
        mx=max(one,mx)
      return mx
