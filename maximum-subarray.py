'''
Problem Link: https://leetcode.com/problems/maximum-subarray/
'''

class Solution:
	'''
	Uses Kadane's algorithm to find the maximum subarray. At every index in the array, the maximum value of the contiguous subarray ending at that index is only either one 
	of the two following: the element in that index itself, or the element in that index plus the maximum value of the contiguous subarray ending at the previous index.

	We keep track of two values: current_max, which is the maximum value of the contiguous subarray ending at an index, and the global_max, which is the overall maximum sum that 
	has been found. At each subsequent interation, we compare the previous current_max with current_max added to the element at the current index, and the new current max is the max
	of these two values. Then we compare global_max to current_max, and if smaller, update global_max to current_max.

	Time Complexity: O(n)
	Space Complexity: O(1)
	'''
    def maxSubArray(self, nums: List[int]) -> int:
	    if max(nums) <= 0:
	            return max(nums)
	    current_max = global_max = nums[0]
	    for i in range(1, len(nums)):
	        current_max = max(nums[i], current_max + nums[i])
	        global_max = max(global_max, current_max)
	    return global_max