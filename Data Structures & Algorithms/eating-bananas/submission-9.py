from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if(len(piles)) == h:
            return max(piles)

        l = 1
        r = max(piles)
        res = r

        while l<=r:
            mid = (l+r)//2
            print("mid in while: ",mid)
            time_to_eat=0

            for i in piles:
                time_to_eat+=ceil(i/mid)

            if time_to_eat <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res