from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_index = {}
            
        for i, num in enumerate(nums):
            if (target - num) in dict_index:
                return [dict_index[target-num], i]
            dict_index[num] = i
        return []