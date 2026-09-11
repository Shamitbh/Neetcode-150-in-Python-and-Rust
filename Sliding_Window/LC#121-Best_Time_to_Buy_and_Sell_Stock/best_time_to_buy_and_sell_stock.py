# 121. Best Time to Buy and Sell Stock
# Difficulty: Medium
# Topics: Array, Dynamic Programming
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
            else:
                l = r
            r += 1
        return max_profit
    
solution_instance = Solution()

case_1_input = [7,1,5,3,6,4]
case_1_output = 5

case_2_input = [7,6,4,3,1]
case_2_output = 0

assert solution_instance.maxProfit(case_1_input) == case_1_output
assert solution_instance.maxProfit(case_2_input) == case_2_output

print("All tests passed successfully!")