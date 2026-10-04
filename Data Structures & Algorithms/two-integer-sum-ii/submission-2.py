class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        value_index = {}
        for i,n in enumerate(numbers):
            if target-n in value_index:
                return[value_index[target-n],i+1]
            
            value_index[n]=i+1
        
            