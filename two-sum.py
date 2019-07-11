'''
Problem Link: https://leetcode.com/problems/two-sum/
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
	'''
	Finds the indices of two values in a list if they add up to a target value.

	Uses a dictionary to store the matching number for any element as its key and the index of the current number as the value. Then,
	when it finds that any subsequent number is already a key in the dictionary, you know that its matching value was already found previously,
	and its index can be gotten from the dictionary, using its own value as the key.
	
	Time Complexity: O(n)
	Space Complexity: O(n)
	'''
	corr = {}
	for i, item in enumerate(nums):
		match = target - item
		corr[match] = i
		if item in corr:
			return [corr[item], i]
