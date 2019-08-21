'''
https://leetcode.com/problems/spiral-matrix/

'''

class Solution:
	'''
	Recursive solution that peels the outer layer of the matrix off one at a time. The base cases
	are 1 row (return the row), 2 rows (return the first row + the reversed second row), 1 
	column (return the first element of every row combined into a list), and 2 columns:
	return the outer layer but don't call the function recursively since there will
	be no columns left. 

	Each call will piece the outer layer by the four pieces: The first row, the 
	last column excluding the first element, the last row in reverse excluding the 
	last element, and the first row in reverse excluding the first and last elements.
	Put these pieces together and then call the function recursively on the matrix
	that is left over, which is the matrix excluding the first and last row and 
	first and last column.

	Time Complexity: O(m*n)
	Space Complexity: O(m*n)
	'''
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        return self.recurse(matrix)
    def recurse(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        if m == 1:
            return matrix[0]
        if m == 2:
            return matrix[0] + matrix[1][::-1]
        if n == 1:
            return [row[0] for row in matrix]
        first = matrix[0]
        second = []
        for i in range(1,m):
            second.append(matrix[i][n-1])
        third = []
        for j in range(n-2,-1,-1):
            third.append(matrix[m-1][j])
        fourth = []
        for i in range(m-2, 0, -1):
            fourth.append(matrix[i][0])
        if n == 2:
            return first + second + third + fourth 
        else:
            return first + second + third + fourth + self.recurse([row[1:-1] for row in matrix[1:-1]])

class Solution:
	'''
	Iterative solution. Set left/right/up/down indices to the outer indices of the matrix,
	then iterate through the first row up to but not including the last element, the last 
	column up to but not including the last element, the last row in reverse up to but not
	including the last element, and then the first column in reverse up to but not including
	the first element. Then increase left and up by 1, and reduce right and down by 1. If 
	we break the while loop with l == r, then we know there is only one column left, and 
	if we break the while loop with u == d, then we know there is only one row left. Handle
	these accordingly by iterating either through the row or the column and appending to
	our answer.

	Time Complexity: O(n*m)
	Space Complexity: O(n*m)
	'''
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        u, d, l, r = 0, m-1, 0, n-1
        res = []
        while l < r and u < d:
            for j in range(l,r):
                res.append(matrix[u][j])
            for i in range(u,d):
                res.append(matrix[i][r])
            for j in range(r,l,-1):
                res.append(matrix[d][j])
            for i in range(d,u,-1):
                res.append(matrix[i][l])
            u, d, l, r = u+1, d-1, l+1, r-1

        if l == r:
            for i in range(u,d+1):
                res.append(matrix[i][r])
        elif u == d:
            for j in range(l,r+1):
                res.append(matrix[u][j])
        return res

        