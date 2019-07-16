'''
Problem Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
'''


class Solution:
	'''
	Uses a modified version of iterative binary search. For any element somewhere in the middle of the array, if that element is less than the element at the end of the array,
	then we are to the right of the pivot, and vice versa. This version keeps two pointers (left and right), and finds the mid-point of the array and compares its value to the end-point. 
	If less, then the pivot is either that value or to its left, so set the right pointer to the midpoint and search again in the left sub-array. If greater, then simply increase the left pointer
	by one, and search again. This ensures our algorithm will not ever skip over the minimum value. Once both pointers are pointing at the same index, we know the minimum is there.

	Time Complexity: O(logn)
	Space Complexity: O(1)
	'''
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[-1]:
                right = mid
            else:
                left += 1
        return nums[left]



class Solution2:
	'''
	Recursive version of the previous solution. Doesn't require passing pointers as arguments. Checks first if both the midpoint value is greater than the value to the right of it, in which case
	the value to the right of it is the minimum. Then checks if the midpoint value is less than the value to the left of it, in which case the midpoint is the minimum value. If neither of these is true,
	then checks if the midpoint value is less than the endpoint value. If so, recursively call the function on the subarray ranging from the start of the passed in array to the midpoint. If not, recursively
	call the function on the subarray ranging from the midpoint to the end of the passed in array.

	Time Complexity: O(logn)
	Space Complexity: O(1)
	'''
	def findMin(self, nums: List[int]) -> int:
	    low, high = 0, len(nums)- 1
	    if low == high:
	        return nums[low]
	    mid = low + (high - low) // 2
	    if nums[mid] > nums[mid+1]:
	        return nums[mid+1]
	    if nums[mid] < nums[mid-1]:
	        return nums[mid]
	    if nums[mid] < nums[high]:
	        return self.findMin(nums[low:mid+1])
	    if nums[mid] > nums[high]:
	        return self.findMin(nums[mid:high+1])