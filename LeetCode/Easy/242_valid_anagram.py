class Solution:
    def isAnagram(self,s,t):
      ds={}
      for i in s:
        ds[i] = ds.get(i, 0) + 1
      dt={}
      for j in t:
        dt[j] = dt.get(j, 0) + 1
      if ds!=dt:
        return False
      return True
