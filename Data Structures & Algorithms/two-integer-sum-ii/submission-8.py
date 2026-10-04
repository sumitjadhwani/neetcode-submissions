class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_ptr, right_ptr = 0, len(numbers) - 1
        
        while left_ptr < right_ptr:
            current_sum = numbers[left_ptr] + numbers[right_ptr]
            
            if current_sum == target:
                return [left_ptr + 1, right_ptr + 1]
            elif current_sum < target:
                left_ptr += 1
            else:
                right_ptr -= 1