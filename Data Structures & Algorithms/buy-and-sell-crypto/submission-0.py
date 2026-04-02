class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        start = prices[0]
        for price in prices[1:]:
            if price - start > profit:
                profit = price - start 
            elif price < start:
                start = price
        return profit   

        