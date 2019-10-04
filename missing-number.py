'''
https://leetcode.com/problems/missing-number/
'''
class Solution:
	'''
	Using Gauss's method for summing a sequence of numbers which is incremented by a constant amount,
	we know that the sum of numbers from 1 to n is (n*(n+1)) / 2. Thus, we know that the expected sum,
	if the sequence wasn't missing a number, would be equal to this formula, where n is the length of the
	input array (since zero is included, otherwise n would be length + 1). Thus, we can simply subtract
	our expected sum with the actual sum of the array to find the missing integer.

	Time Complexity: O(n)
	Space Complexity: O(1)
	'''
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected = (n*(n+1))//2
        return expected - sum(nums)
