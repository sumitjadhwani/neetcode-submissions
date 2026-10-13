class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l,r = 0, len(matrix)-1
        target_list = []
        
        while l<=r:
            mid = l + (r-l)//2
            len_mid_mat = len(matrix[mid])
            if target >= matrix[mid][0] and target <= matrix[mid][len_mid_mat-1]:
                if(target == matrix[mid][0]) or (target == matrix[mid][len_mid_mat-1]):
                    return True
                target_list = matrix[mid]
                break
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1
        
        if target_list:
            print(target_list)
            left, right = 0, len(target_list)-1
        
            while left <= right:
                mid = left + (right - left)//2
                # print(mid)
                
                if target_list[mid] == target:
                    return True
                elif target_list[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return False