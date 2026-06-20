class Solution:
    def isPalindrome(self, x: int) -> bool:
            test=0
            rev=0
            test=x        
            while test>0:               
                rev = 10*rev +(test%10)
                test=test//10
            return x==rev  
