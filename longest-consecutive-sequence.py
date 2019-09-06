'''
https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

'''


class Solution:
	'''
	The key to this problem is realizing that a hashmap yields constant time lookups, and to find if we can continue
	a streak of consecutive elements requires a lookup to see if the current element + 1 exists in the array as well.

	First, convert the array of nums into a set of numbers, which, in Python, is a hashmap-based structure that lets us
	check if an element is in it in constant time. Then iterate through every number in the set. First, check if a number
	one less than that number exists in the set. If so, then move onto the next number. This check is crucial, since we 
	only want to spend time checking a sequence from its lowest starting point.

	For example, if the sequence [4,5,6,7,8,9] exists in a set of 20 numbers, we don't want to have to try checking from 4,
	5, 6, 7, 8, and 9, and can use this quick check to ensure that we only try checking from the lowest value (4). Then, we
	simply have a variable thats tracking the global maximum and a variable thats tracking the length of the current sequence.
	Using a while loop, we check if the current number is in the set, and if so, incease the current sequence length, update
	the maximum sequence length, and increase the number by 1.

	Time Complexity: O(n)
	Space Complexity: O(n)
	'''
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_streak = 0
        for num in nums:
            if num-1 in nums:
                continue
            curr_num = num
            curr_streak = 0
            while curr_num in nums:
                curr_streak += 1
                max_streak = max(curr_streak, max_streak)
                curr_num += 1
        return max_streak






  