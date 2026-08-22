class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        i, j = 0, 1
        while j < len(prices):
            profit = prices[j] - prices[i]
            if profit < 0:
                i = j
                j += 1
                continue
            maxProfit = max(maxProfit, profit)
            j+= 1
        
        return maxProfit