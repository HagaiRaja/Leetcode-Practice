class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = 0
        low = prices[0]
        for price in prices:
            if (price < low):
                low = price
            if (maxPro < price-low):
                maxPro = price-low
        return maxPro