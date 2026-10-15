class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        
        if (nums[l] < nums[r]) or r == 0:
            return nums[0]
        while l<=r:
            mid = (l+r)//2

            if (nums[l] < nums[mid]):
                l = mid
                continue
            elif (nums[mid] < nums[r]):
                r = mid
                continue
            elif (nums[l]==nums[mid]) and (nums[l] > nums[r]):
                return nums[r]
            