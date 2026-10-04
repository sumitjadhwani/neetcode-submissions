class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # largest window of UNIQUE characters

        l = 0
        window = set()
        longest = 0

        for r in range(len(s)):
            if s[r] not in window:
                window.add(s[r])
                longest = max(longest, len(window))
            else:
                # s[r] is IN THE WINDOW
                # remove from the left until it's not
                while s[r] in window:
                    window.remove(s[l])
                    l += 1
                window.add(s[r])
        
        return longest

