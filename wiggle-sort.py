'''
https://www.lintcode.com/problem/wiggle-sort/
'''

class Solution:
    """
    Simple solution where we first sort the nums. Then we visit 
    every odd index in the array, and swap it with its following
    neighbor. Since it's sorted, swapping will guarantee that the
    odd index is greater than or equal the even index. And also that
    the next odd value will be greater than or equal the even value,
    since the array is sorted.

    Time Complexity: O(nlog(n))
    Space Complexity: O(1)
    """
    def wiggleSort(self, nums):
        nums.sort() 
        if len(nums) > 2:
        	for i in range(1, len(nums)-1, 2):
        		nums[i], nums[i+1] = nums[i+1], nums[i]
		

class Solution2:
    """
    If we're considering the number at index i, and we know the previous 
    array is already wiggle-sorted, then all we really have to do is swap
    the current number with the previous number if it breaks the wiggle-sort
    rule, based on whether the index is even or odd. For example, if we've
    seen [3,5] and the next number is 6. Since the index is even(2), it should
    be less than the previous value. It's not, so swap them. This won't break
    the wiggle-sort property with the previous index since we already knew 5
    was >= 3, and since 6 > 5, then 6 is also guaranteed to be >= 3. Simply iterate
    through the array once, check if the index is odd, check if the wiggle sort property
    is valid, and if not swap the elements.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def wiggleSort(self, nums):
        for i in range(1, len(nums)):
            if i % 2:
                if nums[i] < nums[i-1]:
                    nums[i], nums[i-1] = nums[i-1], nums[i]
            else:
                if nums[i] > nums[i-1]:
                    nums[i], nums[i-1] = nums[i-1], nums[i]

		