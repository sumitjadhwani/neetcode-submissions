class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_ptr, right_ptr = 0, len(heights)-1
        res = 0
        while left_ptr != right_ptr:
            temp = heights[right_ptr]*(right_ptr-left_ptr)
            if(heights[left_ptr] > heights[right_ptr]):
                res = temp if temp >res else res
                right_ptr-=1
                continue
            elif(heights[left_ptr] == heights[right_ptr]):
                res = temp if temp >res else res
                left_ptr+=1
                continue
            elif(heights[left_ptr] < heights[right_ptr]):
                temp = heights[left_ptr]*(right_ptr-left_ptr)
                res = temp if temp >res else res
                left_ptr+=1
                continue
        
        return res
