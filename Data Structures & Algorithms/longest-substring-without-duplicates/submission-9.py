class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = [0]*128

        l = 0
        res = 0
        for r in range(len(s)):
            while count[ord(s[r])] > 0:
                count[ord(s[l])]-=1
                l+=1
            count[ord(s[r])]+=1
            res = max(res, r-l+1)
        return res
