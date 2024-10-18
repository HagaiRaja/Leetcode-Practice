class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0]*len(prices) for _ in range(3)]

        for k in range(1, 3):
            minn = prices[0]
            for i in range(1, len(prices)):
                minn = min(minn, prices[i] - dp[k-1][i-1])
                dp[k][i] = max(dp[k][i-1], prices[i] - minn)

        return dp[-1][-1]