import random
class Solution:
    '''
    Iterative quickselect algorithm using a randomly chosen pivot point each iteration.

    Implement kth smallest finder, since sorting in ascending is more intuitive. For example,
    if len(nums) = 6, and we want the 2nd smallest element, it's located at index k-1, so nums[1].
    The 2nd largest element, on the other hand, will be the len(nums) - (k-1) = (6) - (1) = 5th smallest
    element, located at index 4. Once we've figured out the index for the kth largest value in the sorted
    array (len(nums)-k), run the quickselect algorithm.

    Choose a pivot point randomly, and then partition the array around that pivot point. Once partitioned, we
    know that the index of the pivot point is its actual index in the sorted array. If the pivot point index 
    is less than k_idx, re-run the partitioning on the left partition, since k must be in here. If k_idx
    is greater than the pivot index, re-run the partitioning on the right partition, since k must be in here.
    Otherwise, k_idx is the pivot_idx, in which case we've found the kth largest value.

    Time Complexity: Worst O(n^2), Average O(n)
    Space Complexity: O(1)
    '''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        start, end = 0, len(nums)-1
        k_idx = len(nums) - k
        while True:
            piv_idx = random.randint(start,end)
            pivot = nums[piv_idx]
            nums[end], nums[piv_idx] = nums[piv_idx], nums[end]
            i = start-1
            for j in range(start, end):
                if nums[j] < pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[end], nums[i+1] = nums[i+1], nums[end]
            if k_idx > i+1:
                start = i+2
            elif k_idx < i+1:
                end = i
            else:
                return nums[i+1]
