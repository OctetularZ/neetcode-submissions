class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        max_profit = 0

        left, right = 0, 0

        while left < len(prices) and right < len(prices):
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)

            if right < len(prices) - 1 and prices[right] > prices[right + 1]:
                print(prices[right], prices[right + 1])
                res += max_profit
                max_profit = 0
                left = right = right + 1
                continue
            
            right += 1
        
        return res + max_profit


# What has worked from small tests sizes, I doubt it'll work with all test cases:
    # Use two pointers (both begin from the start)
    # If right is smaller than left, move left to right position
    # Otherwise, keep moving right and re-evaluating max profit
    # When value just after right position is smaller, move left pointer and right pointer to that position.
