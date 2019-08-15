'''
https://leetcode.com/problems/jump-game/

'''

class Solution:
	'''
	If we know we can reach index i from our current position by jumping, then we can reach index i-1, i-2, ..., etc. by jumping. 
	If we iterate through the input array, we can calculate the maximum jump index from the current position by simply adding our current 
	index plus the value at that element of our array. At this point, we know that all elements up to max_jump_idx are visitable, since if we
	can visit max_jump_idx, we can visit all the indices between our current position and max_jump_idx. As we visit a new position,
	we can always update the max_jump_idx to the maximum between the current max_jump_idx, and the current position index plus
	the value at that position. 

	Then, during our iteration, we just need to check for two things. If our current position is ever greater than max_jump_idx, then
	a path to this position does not exist, so we can return False. If max_jump_idx is ever >= the last index (len(nums)-1), then we 
	know we can make it to the end of the array, so return True.

	Time Complexity: O(n)
	Space Complexity: O(1)
	'''
    def canJump(self, nums: List[int]) -> bool:
        max_jump_idx = 0
        for i in range(len(nums)):
            if i > max_jump_idx:
                return False
            if max_jump_idx >= len(nums)-1:
            	return True
            max_jump_idx = max(max_jump_idx, i + nums[i])
        return True if max_jump_idx >= len(nums)-1 else False

class Solution2:
	'''
	Top-down dynamic programming solution (fails as Memory Limit Exceeded on leetcode for massive input tests due to recursion depth exceeded). 
	Every time we make a jump we are moving to a smaller subproblem of the same nature. We want to build a recursion tree from the start of the array,
	where every branch is a potential path that is moving towards the end of the array. If the branch reaches a recursion call on an array 
	of length one, then we have reached our base case of a valid path, and we return True. 

	Then, we simply have to iterate through all possible leaps from 1 to max_leap, where max_leap is either the number in our current value, or,
	if that number exceeds the end of our array, then we know we have a solution and can return True. At each iteration, we call our function
	recursively on the rest of the array from the point we jumped to from the current position. If any of these recursive calls returns True,
	then we know that there is a valid path and can return True. If we try all possible paths from our current position and none of them
	return True, then we can return False.

	We use a memoization dictionary to avoid overlapping subproblems, using the length of n as our key, since all subproblems have to end at the same
	spot, any subproblem called on an array of the same length is the same subproblem.

	Time Complexity: O(n^2)
	Space Complexity: O(n)
	'''
    def __init__(self):
        self.memo={}
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        if n == 0:
            return False
        max_leap = nums[0]
        if max_leap > n-1:
            return True
        if n not in self.memo:
            for i in range(1,max_leap+1):
                is_valid = self.canJump(nums[i:])
                if is_valid:
                    self.memo[n] = True
                    return True
            self.memo[n] = False
            return False
        return self.memo[n]


class Solution3:
	'''
	Bottom-up DP solution (fails Time Limit Exceeded). Create a DP array of booleans set to all False except for the first value. The value at each index will be set to True
	if we can each that index by jumping from a prior index. Then, iterate through the array. The variable max_leaps indicates the value of nums at
	this index. From the index we are at, if the index of the DP array is True at that index (meaning we we're able to reach this point from a previous jump), 
	go to the next max_leaps indices, and set them to True, or simply return True if i + max_leaps reaches the end of the array. 

	Finally, return the last value in dp, which will be True, if we we're able to find a valid path here.

	Time Complexity: O(n^2)
	Space Complexity: O(n)
	'''
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False 
        dp = [False] * len(nums)
        if nums[0] > 0 or len(dp) == 1:
            dp[0] = True
        for i in range(len(dp)-1):
            if dp[i]:
                max_leaps = nums[i]
                if i + max_leaps >= len(nums):
                    return True
                for j in range(i+1,i+max_leaps+1):
                    dp[j] = True
        return dp[-1]



