class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        day_sell, day_buy = 1, 0
        maxProfit = 0
        while day_sell < len(prices):
            profit = prices[day_sell] - prices[day_buy]
            if profit < 0:
                day_buy = day_sell
                day_sell += 1
            else:
                maxProfit = max(maxProfit,profit)
                day_sell += 1
        
        return maxProfit