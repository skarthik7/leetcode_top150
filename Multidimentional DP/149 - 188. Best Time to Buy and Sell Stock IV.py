class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0

        n = len(prices)
        if k >= n // 2:
            profit = 0
            for i in range(1, len(prices)):
                profit += max(prices[i] - prices[i - 1], 0)
            return profit 
        dp = []
        for i in range(k + 1):
            dp.append([0] * n)
        for i in range(1, k + 1):
            max_diff = -prices[0]  
            for j in range(1, n):
                dp[i][j] = max(dp[i][j-1], prices[j] + max_diff) 
                max_diff = max(max_diff, dp[i-1][j] - prices[j]) 

        return dp[k][n-1]