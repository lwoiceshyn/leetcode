'''
https://leetcode.com/problems/maximal-square/
'''


class Solution:
	'''
	If the current element is a 1 and the element to the left, the element above, and the element to the top left
	are all bottom-right corners of squares, the current element is the bottom-right element of a square, and the length
	of the square ending in that element is 1 + the minimum length of the squares in the three previously mentioned tiles.

	Thus, the matrix can act as a sort-of bottom-up dynamic programming array, where the element represents the longest square
	that the element is the bottom-right corner of. If we iterate from top left to bottom right, we can continually populate each
	element with the longest square that ands in that element. For each element, check if both i and j are > 0 (so that we can index
	into the left, top, and top left elements), and check if that element is 1 (so it's eligible to be part of a square). If these
	conditions are met, then set the element to itself + the minimum of the top-left, left, and top elements.

	For some reason, this problem has the elements as strings, making things messy.

	Time Complexity: O(m*n)
	Space Complexity: O(1)
	'''
	def maximalSquare(self, matrix: List[List[str]]) -> int:
	    if not matrix or not matrix[0]:
	        return 0
	    m, n = len(matrix), len(matrix[0])
	    max_length = 0
	    for i in range(m):
	        for j in range(n):
	            if i and j and int(matrix[i][j]):
	                matrix[i][j] = int(matrix[i][j]) + \
	                min(int(matrix[i-1][j]), int(matrix[i][j-1]), int(matrix[i-1][j-1]))
	            max_length = max(max_length, int(matrix[i][j]))
		return max_length ** 2