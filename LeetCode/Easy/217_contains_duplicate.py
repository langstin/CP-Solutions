class Solution:
    def containsDuplicate(self, nums):
      dup=set()
      for i in range(len(nums)):
        if nums[i] in dup:
          return True
        else:
          dup.add(nums[i])
      return False
