'''
Problem Link: https://leetcode.com/problems/contains-duplicate/
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
    	'''
		Uses a set and checks if each subsequent value is already in the set or not.

		Time Complexity: O(n)
		Space Complexity: O(n)
    	'''
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            else:
                num_set.add(num)
        return False

'''
This is a slightly more elegant solution which does the same thing.
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
    	return len(nums) > len(set(nums))