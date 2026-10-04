class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
         SetNums = set(nums)
                 
         return(len(SetNums) < len(nums))
        


        
