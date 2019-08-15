'''
https://leetcode.com/problems/combination-sum-iv/submissions/
'''

class Solution:
	'''
	Top-down dynamic programming solution. Create a recursion tree starting from the target value by subtracting all of the numbers in the array from it. The base cases
	are f(nums, target=0) = 1, in the case in which we were able to find a combination that adds to it, and f(nums, target<0) = 0 in the case where we reach a dead end.
	For each function call, we go through each of the numbers in nums and create a branch, and then sum all of the values returned from that branch, which will equal
	all of the combinations that added up the amount. The initial function call will return the total number of combinations, with repetition allowed, that add up to our target.
	If repetition was not allowed we would need some method, such as a set, to ensure that we don't included repeated sets of nums.
	
	A memoization dictionary is used to handle the overlapping subproblems.

	Time Complexity: O(target * nums)
	Space Complexity: O(target)
	'''
    def __init__(self):
        self.memo = {}
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        if target == 0:
            return 1
        if target < 0:
            return 0
        if target not in self.memo:
            total = 0
            for num in nums:
                total += self.combinationSum4(nums, target-num)
            self.memo[target] = total
        return  self.memo[target]


class Solution:
	'''
	Bottom-up dynamic programming solution. Initialize a DP array of length target + 1, of zeros, and setting the zero-indexed value to 1.
	The value at element i of the DP array is the total number of ways we can sum values in nums to get to that amount, thus tracking the total
	number of combinations that can be used to reach that value. We simply iterate through the DP array once, and at each iteration, going through
	each of the numbers in nums, and adding dp[i-num] to dp[i], checking to make sure we don't index out of bounds (i >= num). Finally, we return the 
	last value in dp, which will be the total number of combinations we can make that sum up to the target value. If the number cannot be reached by summing
	the numbers in nums, then the value at dp[target] will remain 0.
 
	Time Complexity: O(target * nums)
	Space Complexity: O(target)
	'''
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        dp = [0] * (target+1)
        dp[0] = 1
        for amount in range(1,len(dp)):
            for num in nums:
                if amount >= num:
                    dp[amount] = dp[amount] + dp[amount-num]
        return dp[-1]