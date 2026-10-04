class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_seq_length=0
        occ_nums = {}
        for n in nums:
            occ_nums[n] = 1

        for n in nums:
            temp_length=1
            # print("n:", n)
            if n+1 in occ_nums and n-1 not in occ_nums:
                temp = n+1
                # print("temp", temp)
                while temp in occ_nums:
                    # print("inside while temp: ",temp)
                    temp_length+=1
                    temp=temp+1
            if temp_length > max_seq_length:
                max_seq_length=temp_length
            # print("temp_length: ",temp_length)
            # print("max_seq_length: ",max_seq_length)
        return max_seq_length
