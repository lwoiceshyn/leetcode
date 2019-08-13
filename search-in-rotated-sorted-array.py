'''
https://leetcode.com/problems/search-in-rotated-sorted-array/
'''	

class Solution:
	'''
	A modified version of iterative binary search. Every time we split an array into halves, one of the two halves will be properly sorted, while the other will have 
	the pivot point in it. We can perform a simple check to see if we are in a properly sorted subarray by comparing the first and last value of the subarray,
	and seeing if the left value is less than the right value. In this case, we can simply proceed with binary search until we either find or don't find our value.
	Otherwise, one of our two halves will be guaranteed to be sorted. Since we're finding the median, we can check if the array from left to the median, or the array
	from the median to the right is sorted. For whichever of these is sorted, simply compare the left and right values to the target. If target is in this subarray, then
	reassign indices to search within this subarray and perform simple binary search. Otherwise, reassign indices to the other half subarray and perform this logic again.

	Time Complexity: O(log(n))
	Space Complexity: O(1)
	'''
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if nums[0] == target:
            return 0
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            if nums[left] < nums[right]:
                if nums[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
            else:
                if nums[left] < nums[mid]:
                    if target > nums[left] and target < nums[mid]:
                        right = mid-1
                    else:
                        left = mid+1
                else:
                    if target > nums[mid] and target < nums[right]:
                        left = mid+1
                    else:
                        right = mid-1
        return -1