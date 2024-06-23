class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        buy1= float('-inf')
        sell1 = 0
        buy2 = float('-inf')
        sell2 = 0
        
        for price in prices:
            sell2 = max(sell2, buy2 + price)
            buy2 = max(buy2, sell1 - price)
            sell1 = max(sell1, buy1 + price)
            buy1 = max(buy1, -price)

        return sell2

# Time complexity: O(N)