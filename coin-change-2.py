'''
https://leetcode.com/problems/coin-change-2/

'''


class Solution(object):   
	'''
	Top-down dynamic programming solution. We can continuously break the original problem into subproblems of the following nature: One solution
	set which includes at least one of a certain denomination of coin, and one which doesn't include this denomination. Then, we can sum up each of
	these sets to get the total unique ways to sum to the desired amount. 

	The recursive formulation is as follows: f(amount, coins) = f(amount - coin[-1], coins) + f(amount, coins[:-1]). We can continually do this,
	creating a recursion tree, until we reach one of our base cases. If amount is 0, then we have found a solution, so return 1. If amount is < 0,
	that means that we tried to use a denomination larger than the amount, so this set didn't work. If coins is empty, then we reached the case where
	there are no more denominations left, so also return 0. Then, at every node, we simply sum up the number of unique solutions for the two sets branching
	from that node as they return values, leaving us with the total number of unique solutions for the original amount and list of coin denominations
	from our first function call.

	Time Complexity: O(coins * amount)
	Space Complexity: O(coins * amount)
	'''
    def change(self, amount, coins):
        self.memo = {}
        self.coins = coins
        self.coins.sort()
        return self.recurse(amount, len(coins)-1)
    def recurse(self, amount, index):
        if amount == 0:
            return 1
        if amount < 0 or index < 0:
            return 0
        key = str(amount) + '-' + str(index)
        if key not in self.memo:
            self.memo[key] = self.recurse(amount - self.coins[index], index) + self.recurse(amount, index-1)
        return self.memo[key]

class Solution(object):   
	'''
	Bottom-up dynamic programming solution. First consider a dp array of dimensions len(coins)+1 x amount+1, where dp[index][amount] will represent the number of 
	unique ways in which we can sum to that amount using all coins in coins[:index]. We start with the base cases of amount=0, where dp[:][0] = 1, and using none
	of our denominations, where dp[0][:] = 0 (except for dp[0][0] which is 1). Then, we can build up our array by iterating first through our rows, starting with
	the second row, where we have one coin, and then setting dp[index][amount] = dp[index - 1][amount] + dp[index][amount-coin[index]]. The first term represents
	the unique ways we were able to make that amount prior to introducing the current coin, and the second way adds the current coin to the number of
	ways we can make amount-coin, including ways using the current coin. As we add one coin at a time, we ensure that we only consider unique ways of adding
	coins to make each amount. 

	Since each iteration simply builds on the previous row of the dp table, we only need to store one row in memory, and then update this row based on the previous
	value in each element, plus the additional solutions which the new coin adds to it. In our inner for loop, we start from the coins value, since we don't
	want to index outside of the dp array.

	Time Complexity: O(coins * amount)
	Space Complexity: O(amount)
	'''
    def change(self, amount, coins):
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
        	for i in range(c, len(dp)):
    			dp[i] += dp[i-c]
       	return dp[-1]