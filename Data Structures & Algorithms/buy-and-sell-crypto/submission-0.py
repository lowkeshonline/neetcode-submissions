class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_so_far = 0

        for i in range(len(prices)):
            
            for j in range(i + 1, len(prices)):

                if i == j:
                    continue

                curr_profit = prices[j] - prices[i]

                max_so_far = max(curr_profit, max_so_far)

        return max_so_far

        