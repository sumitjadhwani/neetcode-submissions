class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
         DictNums = {}
                 
         for num in nums:
            if(num not in DictNums): 
                DictNums[num]= 0
            DictNums[num] += 1

            if(DictNums[num] > 1): return True

         return False
        


        
