class Solution:
  def longestCommonPrefix(self, s):       
   l=""
   i=0
   k=True
   while k==True:    
           for j in range(len(s)):
             try:                 
               t=True
               if i>(len(s[j])-1):
                   t=False
                   break             
               elif j==(len(s)-1):                       
                   break
               elif s[j][i]!=s[j+1][i]:
                   t=False
                   break                                      
             except IndexError:
                 t=False
                 k=False
                 break
           if t==True:             
                l+=s[j][i]
           else:
               break                                  
           i+=1
   return l 
