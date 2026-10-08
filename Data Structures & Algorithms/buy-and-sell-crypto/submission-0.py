class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        profit, diff = 0, 0
        for p in prices:
            if p < low:
                low = p
            else:
                diff = p - low
            if diff > profit:
                profit = diff
        return profit