class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n]=1
            else:
                return True
        return False