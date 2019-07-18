'''
Problem Link: https://leetcode.com/problems/container-with-most-water/
'''

class Solution:
	'''
	The formula for the are between two indices is defined as min(arr[left], arr[right]) * (right-left). If we start considering the entire array,
	the only way that we find a larger area by decreasing the width is through increasing the height at one of the indices. Therefore, we assign pointers
	at each end of the array. While the pointers haven't met, calculate the area using the formula, and then shift the pointer with the smaller height. If same
	height, shift either one arbitrarily.

	Time Complexity: O(n)
	Space Complexity: O(1)
	'''
    def maxArea(self, height: List[int]) -> int:
        left = max_area = 0
        right = len(height) - 1
        while left < right:
            curr_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, curr_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
