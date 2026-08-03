class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = 0
        sell = 1
        max_so_far = 0

        while (buy < len(prices) and sell < len(prices)):

            curr_price = prices[sell] - prices[buy]

            max_so_far = max(curr_price, max_so_far)

            if prices[sell] < prices[buy]:
                buy = sell
            
            sell += 1
        
        return max_so_far

        