class Solution:
	'''
	Bottom-up dynamic programming solution. We want to modify the array in place such that nums[i] will change to the maximum sum we can achieve through
	any combination of values in the range [0,i] while following the adjacency rule. The recurrence relation is f(n) = max(f(n-1), f(n)+f(n-2)), since f(n)
	will be initialized to the house value at that location. The crucial step here is since we iterate starting at 2 to avoid zero-index errors, we need to 
	make sure we set nums[1] to its appropriate maximum value, which is simply the max between nums[1] and nums[2]. 
	
	This is important in cases such as [2,1,1,2], where the max sum is between index 0 and index 4, which would not give us the correct output if we did not do this step.

	Time Complexity: O(n)
	Space Complexity: O(1)
	'''
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        nums[1] = max(nums[0], nums[1])
        for i in range(2,len(nums)):
        	nums[i] = max(nums[i-1], nums[i]+ nums[i-2])
        return nums[-1]

class Solution:
	class Solution:
	'''
	Top-down dynamic programming solution, with the same formulation as above. We start at the end of the array, and work our way towards the beginning. Our two base 
	cases are when the length of the list we pass in is 1, in which case were simply returning the value in the list, or 2, in which we return the max of the two values.
	The recursive formula is as follows: f(n) = max(f(n-1), f(n) + f(n-2)). We use a memoization dictionary to avoid redundant computations of overlapping subproblems,
	and use the length of the list, n, as the key, to ensure linear space complexity.

	Time Complexity: O(n)
	Space Complexity: O(n)
	'''
    def __init__(self):
        self.memo = {}
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        if n not in self.memo:
            self.memo[n] = max(self.rob(nums[:-1]), nums[-1] + self.rob(nums[:-2]))
        return self.memo[n]