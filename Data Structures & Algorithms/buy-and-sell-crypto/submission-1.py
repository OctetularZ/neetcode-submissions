class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = float('-inf')
        min_buy = float('inf')

        for i in range(len(prices)):
            min_buy = min(prices[i], min_buy)
            max_profit = max(max_profit, prices[i] - min_buy)
        
        return max_profit