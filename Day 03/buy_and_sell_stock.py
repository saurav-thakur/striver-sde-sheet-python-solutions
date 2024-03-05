class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_val = prices[0]
        max_profit = 0

        for i in range(1,len(prices)):
            min_val = min(prices[i],min_val)
            profit = prices[i] - min_val
            max_profit = max(profit,max_profit)
        return max_profit
