'''
https://leetcode.com/problems/set-matrix-zeroes/

'''


class Solution:
	'''
	Simply go through all elements, and if zero, add to a set tracking which columns and
	rows need to be zero. Then, go through the rows that need to be zero, and each element
	in the row, and set to zero, then go through the columns that need to be zero, and each
	element in that column, and set to zero.

	Time Complexity: O(m*n)
	Space Complexity: O(m+n)
	'''
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        zero_cols = set()
        zero_rows = set()
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_cols.add(j)
                    zero_rows.add(i)
        for i in zero_rows:
            for j in range(cols):
                matrix[i][j] = 0
        for j in zero_cols:
            for i in range(rows):
                matrix[i][j] = 0
        return matrix

class Solution(object):
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Rather than tracking the zero rows and columns in separate sets, we use the first element 
        in each row or column to indicate if every element in that row or column should be set to 
        zero. The only issue that arises here is that if the element [0][0] is set to zero, we don't
        know if that means the first row or first column should be set to zero. To solve this,
        assume [0][0] being zero only means that the first row should be zeros, and use a separate
        variable col_zero to indicate the first column should be zeros. First, go through the first row and column,
        and set col_zero to zero or matrix[0][0] to zero, if necessary. Then, iterate through the matrix from top
        left to bottom right, and set all the first-row and first-column values to zero, as necessary. Do not set matrix[0][0]
        to zero if j = 0, since col_zero is the variable tracking this. Then, iterate through the matrix
        from the bottom up (since we don't want to affect the first row and column of the matrix until
        all of the other values are set properly). Then lastly, go through the first row and column,
        if they should be set to zero, and set them to zero.

    	Time Complexity: O(m*n)
		Space Complexity: O(1)
        """
        m = len(matrix)
        n = len(matrix[0])
        col_zero = 1
        for i in range(m):
            if matrix[i][0] == 0:
                col_zero = 0
        for j in range(n):
            if matrix[0][j] == 0:
                matrix[0][0] = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0 and j != 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(m-1,0,-1):
            for j in range(n-1,0,-1):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0
        if not col_zero:
            for i in range(m):
                matrix[i][0] = 0
        return matrix

