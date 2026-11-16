class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minstart = prices[0]
        profit = 0
        for i in range(len(prices)):
            if prices[i]<minstart : minstart = prices[i]
            prof = prices[i]-minstart
            profit = max(prof,profit)
        return profit