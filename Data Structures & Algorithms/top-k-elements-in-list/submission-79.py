class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ = [[] for _ in range(len(nums)+1)]
        count = defaultdict(list)
        # print(occ)
        print(nums)

        for num in nums:
            if(num not in count): 
                count[num] = 0
            count[num] += 1
        # print(count)
        for key in count:
            occ[count[key]].append(key)

        # print(occ)
        res = []
        i = 1
        for sub_list in occ[::-1]:
            if(len(sub_list)>0): 
                for ele in sub_list:
                    res.append(ele)
                    i += 1
            if(i>k): 
                break
        return res
        