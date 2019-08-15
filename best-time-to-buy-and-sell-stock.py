'''
Problem link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Keeps track of two values: the current minimum, and the current maximum profit. Every value in the iteration is first used to calculate the profit and compared to the current max profit,
        and then compared to the current minimum and replaces it if smaller.

        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        if len(prices) == 0:
            return 0
        curr_min = prices[0]
        curr_max_profit = -float('inf')
        for i in range(1,len(prices)):
            curr_max_profit = max(curr_max_profit, prices[i] - curr_min)
            curr_min = min(curr_min, prices[i])
        return curr_max_profit if curr_max_profit > 0 else 0