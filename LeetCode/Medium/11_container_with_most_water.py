class Solution:
    def maxArea(self, s: List[int]) -> int:
          a=0
          i=0
          j=len(s)-1
          while not i>j:
              test=min(s[i],s[j])*(j-i)
              if s[i]>s[j]:
                  j-=1
              elif s[i]==s[j]:
                  i+=1
                  j-=1                                  
              else:
                  i+=1
              if test>a:
                  a=test                                          
          return a        
