class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        l = 0
        r = 1
        maxProfit = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, profit)

            if prices[r] < prices[l]:
                l = r
            r += 1

        
        return maxProfit