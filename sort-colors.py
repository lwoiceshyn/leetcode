'''
https://leetcode.com/problems/sort-colors/
'''

class Solution:
	'''
	Simple dutch partitioning solution, similar to quicksort partitioning with buckets at both ends.
	As we iterate through the array, we want to store all of the 0s we've found in the left side of
	the array, and all the 2s we've found in the right side of the array. The left pointer will point
	to the first index on the left which does not yet contain a 0, and the right pointer will point
	to the first index on the right which does not yet contain a 2. Iterate through the unsorted 
	array from left to right. When we encounter a 0, swap it with the left pointer value, then increment
	both the left and the iterating pointer. When we encounter a 2, swap it with the right pointer value,
	then decrement the right pointer value. When our iterating pointer passes the right pointer, we've
	fully sorted the array into the three partitions, so end the while loop.

	Time Complexity: O(n)
	Space Complexity: O(1)
	'''
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r, i = 0, len(nums)-1, 0
        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else:
                i += 1
        return nums