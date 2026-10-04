class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = {}
        res = 0
        l=0
        for r in range(len(s)):
            if s[r] in ss:
                l = max(ss[s[r]]+1,l)
            ss[s[r]] = r
            res = max(res,r-l+1)
        return res
