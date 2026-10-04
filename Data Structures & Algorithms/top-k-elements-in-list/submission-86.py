class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            count = {}
            freq = [[] for _ in range(len(nums)+1)]
            res = []
            for num in nums:
                if num not in count:
                    count[num] = 1
                else:
                    count[num]+=1
            
            for num, frequency in count.items():
                freq[frequency].append(num)
            
            for i in range(len(freq)-1,0,-1):
                for num in freq[i]:
                    res.append(num)
                    if len(res) == k:
                        return res
