class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        noOfZeros = 0
        zeroIndex = -1
        res = []
        for i, n in enumerate(nums):  
            if(n == 0):
                noOfZeros += 1
                zeroIndex = i
                continue
            product *= n
        
        if(noOfZeros > 1):
            return [0]*len(nums)

        if(noOfZeros == 1):
            res = [0 for _ in range(len(nums))]
            res[zeroIndex]=product
            return res      


        for n in nums:
            res.append(int(product/n))

        return res
        
