class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            count = {}
            freq = [[] for _ in range(len(nums)+1)]
            res = []
            for i in nums:
                if i not in count:
                    count[i] = 1
                else:
                    count[i]+=1
            # print(count)
            
            for key, value in count.items():
                # print(key, value)
                freq[value].append(key)
            # print(freq)
            
            for i in range(len(freq)-1,0,-1):
                # print(i)
                for num in freq[i]:
                    # print(num)
                    res.append(num)
                    if len(res) == k:
                        return res
