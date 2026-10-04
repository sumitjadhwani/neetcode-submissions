class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_char = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in unique_char:
                unique_char.remove(s[l])
                l=l+1
            unique_char.add(s[r])

            res = max(res, r - l + 1)
        return res