class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1, p2 = 0, 1
        max_profit = 0
        while p2 < len(prices):
            profit = prices[p2] - prices[p1]
            if profit < 0:
                p1 = p2
            max_profit = max(profit, max_profit)
            p2 += 1
        
        return max_profit

