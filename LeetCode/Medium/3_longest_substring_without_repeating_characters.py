class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        p= 0
        mx = 0
        for i in range(len(s)):
            if s[i] in d and d[s[i]] >= p:
                p= d[s[i]] + 1
            d[s[i]] = i
            mx = max(mx, i-p + 1)
        return mx    

