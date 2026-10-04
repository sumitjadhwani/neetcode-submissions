from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_counter = {}
        
        for num in nums:
            if num not in freq_counter:
                freq_counter[num]=1
            else:
                return True
        return False


# nums = input().split(' ')
# nums  = [int(num) for num in nums]

# s = Solution()
# res = s.hasDuplicate(nums)
# print(res)