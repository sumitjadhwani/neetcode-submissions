class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums.sort()
        for i in range (len(nums)):
            if((target - nums[i]) in nums):
                j = nums.index(target - nums[i])
                if(i == j): continue
                if(i > j): return [j, i]
                return [i, j]
        
         