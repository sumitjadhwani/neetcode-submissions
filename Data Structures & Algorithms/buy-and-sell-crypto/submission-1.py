class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(0, len(prices)):
            for j in range(0, len(prices)):
                if(i>j):
                    if (prices[i] - prices[j]) > maxProfit:
                        maxProfit = prices[i] - prices[j]
                    
                else:
                    continue
        return maxProfit