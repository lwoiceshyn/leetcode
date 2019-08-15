'''
https://leetcode.com/problems/coin-change/
'''

class Solution:
	'''
	This is the greedy solution for the problem (not accepted by Leetcode). We sort the coins in descending order, and then 
	find how many of the largest denomination we can divide into the amount, until we can no longer use that denomination,
	and then move onto the next largest denomination, and keep doing that for all of our coins. This solution will only work
	for certain sets of denominations, such as for US coins ([1,5,10,25]). You can see that by examining the case where our amount
	is 63, and we add a 21-cent coin to our US coin denominations ([1,5,10,21,25]). The optimal solution is just 3 of the 21-cent coins, 
	but this algorithm will always start with the largest coin and won't find the best solution.
	
	Time Complexity: O(coins)
	Space Complexity: O(1)
	'''
	def coinChange(self, coins: List[int], amount: int) -> int:
	    coins.sort(reverse=True)
	    num_coins = 0
	    while amount > 0:
	        for coin in coins:
	            if amount >= coin:
	                amount -= coin
	                num_coins += 1
	                break
	    return num_coins


class Solution2:
	'''
	Top-down dynamic programming solution. The recursive formulation is as follows: f(coins, amount) = 1 + min(f(coins, amount-coin) for coin in coins).
	We build a recursion tree starting from our target amount. At each node, create leaf nodes by subtracting each coin amount from the current amount, 
	and then taking the minimum of all the returned values from each leaf, adding 1 to that value since one coin is being used. A memoization table is
	used to avoid redundant computations, as there will be many overlapping subproblems. The base case is simply f(coins, 0) = 0. We return a value of
	infinity if we call the function on an amount < 0, as this path is a dead end, with no remaining denominations dividing into the remaining amount. 
	We need a separate wrapper function to be able to return -1 when no solution is found, which is the case when our returned amount is infinity.
	
	Time Complexity: O(coins * amount)
	Space Complexity: O(amount)
	'''
    def coinChange(self, coins: List[int], amount: int) -> int:
        least_coins = self.helper(coins, amount, dict())
        return least_coins if least_coins < float('inf') else -1
    
    def helper(self, coins, amount, memo):
        if amount < 0:
            return float('inf')
        elif amount == 0:
            return 0
        else:
            if amount not in memo:
                memo[amount] = 1 + min([self.helper(coins, amount-c, memo) for c in coins])
            return memo[amount]


class Solution3:
	'''
	Bottom-up dynamic programming solution. We use an array of length amount + 1 (since we're zero-indexed) to store our minimum number of coins to reach each amount value.
	The index of the array, i, will be the amount, and the value at each index will be the minimum number of coins to reach this amount. We simply need to iterate through
	the array once, and at every index, compare the current value to 1 + the value at the current index minus the coin amounts for each coin, and store the minimum between
	those two values at the index. We use the if statement (c <= i) to make sure that subtracting the coin value from the current index won't go past the beginning of the
	array.
	
	Time Complexity: O(coins * amount)
	Space Complexity: O(amount)
	'''
    def coinChange(self,  coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for i in range(1,len(dp)):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], 1 + dp[i-c])
        return -1 if dp[amount] == float('inf') else dp[amount]