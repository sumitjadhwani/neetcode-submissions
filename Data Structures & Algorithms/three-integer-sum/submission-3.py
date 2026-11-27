class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            # 1. Skip duplicate first numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 2. Standard Two Sum II on the remaining right side
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    # 3. Skip duplicate second numbers
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res