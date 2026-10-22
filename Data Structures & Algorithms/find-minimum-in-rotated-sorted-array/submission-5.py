class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        # Binary search loop
        while l < r:
            mid = (l + r) // 2
            
            # If mid element is greater than the rightmost element,
            # the minimum element must be on the right side.
            if nums[mid] > nums[r]:
                l = mid + 1
            # Otherwise, the minimum is either at mid or to its left.
            else:
                r = mid
                
        # When l == r, they point to the minimum element.
        return nums[l]
