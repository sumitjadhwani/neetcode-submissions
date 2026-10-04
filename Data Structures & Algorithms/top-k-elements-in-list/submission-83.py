class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = count.most_common(k)
        # print(res)
        op = []
        for itr in res:
            op.append(itr[0])
        return op  