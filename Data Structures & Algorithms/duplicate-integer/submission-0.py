class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
         for i in nums:
            count = 0
            for j in nums:
                if(i == j):
                    count += 1
            if(count > 1): return True
            
         return False
        
