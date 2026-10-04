from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_index = {}
        for i, num in enumerate(nums):
            dict_index[num] = i
            
        for i, num in enumerate(nums):
            if (target - num) in dict_index and i!=dict_index[target-num]:
                return [i,dict_index[target-num]]
        