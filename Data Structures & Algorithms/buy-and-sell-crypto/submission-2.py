class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price  # Found a cheaper day to buy
            else:
                max_profit = max(max_profit, price - min_price)  # Try selling today

        return max_profit