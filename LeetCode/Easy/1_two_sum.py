class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
           a=target-nums[i]
           if a in d:
             out=[d[a],i]
             break
           d[nums[i]]=i
        return out
