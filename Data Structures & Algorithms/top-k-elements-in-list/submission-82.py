class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        res = []
        for x in nums:
            if x not in dict:
                dict[x]=1
            else:
                dict[x]+=1
        
        sorted_dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=True)}

        for x in sorted_dict.keys():
            if k!=0:
                res.append(x)
            elif k==0:
                break
            k-=1
        
        return res