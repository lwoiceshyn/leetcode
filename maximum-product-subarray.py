'''
Problem Link: https://leetcode.com/problems/maximum-product-subarray/
'''


Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

class Solution:
	'''
	Uses Kadane's algorithm to find the maximum product subarray. At every index in the array, the maximum value of the contiguous subarray ending at that index one of the three following: 
	the element in that index itself, the element index multiplied by the maximum value of the contiguous subarray ending at the previous index,or the element index multiplied by the minimum
	value of the contiguous subarray ending at the previous index (in the case where the current element is negative and the previous minimum is negative).

	We keep track of three values: current_max, which is the maximum value of the contiguous subarray ending at an index, current_min, which is the minimum value of the contiguous subarray
	ending at an index, and the global_max, which is the overall maximum product that has been found. At each subsequent interation, we compare the previous current_max and current_min
	with their updated products with the new element, and the new value are the max/min of either the current element, the previous max multiplied by the current element, and the previous min
	multiplied by the current element. Then we compare global_max to current_max, and if smaller, update global_max to current_max.

	Note that simultaneous assignment of current_max and current_min is necessary since they are both a function of the values from the last timestep that we don't want to modify until
	we calculate each of them.

	Time Complexity: O(n)
	Space Complexity: O(1)
	'''
    def maxProduct(self, nums: List[int]) -> int:
        current_max = current_min = global_max = nums[0]
        for i in range(1, len(nums)):
            current_max, current_min = max(nums[i], current_max*nums[i], current_min*nums[i]), min(nums[i], current_max*nums[i], current_min*nums[i])
            global_max = max(global_max, current_max)
        return global_max