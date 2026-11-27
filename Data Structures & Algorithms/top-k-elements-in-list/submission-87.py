class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        freq = [[] for _ in range(len(nums)+1)]
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for x in range(len(freq)-1, 0, -1):
            for n in freq[x]:
                if len(res) == k:
                    break
                res.append(n)
        return res

