class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prd_left = []
        prd_right = [1]*len(nums)

        for i, n in enumerate(nums):
            if(i==0):
                prd_left.append(1)
            else:
                prd_left.append(nums[i-1]*prd_left[i-1])

        for i in range(len(nums)-1, -1, -1):
            # print(i)
            if(i==len(nums)-1):
                prd_right[i]=1
            else:
                # print(prd_right, i)
                prd_right[i]=nums[i+1]*prd_right[i+1]

        res = []
        
        for i in range(len(nums)):
            res.append(prd_left[i] * prd_right[i])
        return(res)