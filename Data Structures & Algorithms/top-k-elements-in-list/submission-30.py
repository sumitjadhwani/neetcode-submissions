class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ = {} 
        for num in nums:
            if(num not in occ): occ[num] = 0
            occ[num] += 1
        # res = []
        # res = []
        
        res = sorted(occ.items(), key=lambda x: x[1],reverse=True)
        # print(res)

        count=0
        result = []
        for i in res:
            if(count<k): 
                result.append(i[0])
                count += 1

        return result
        