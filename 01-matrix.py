'''
https://leetcode.com/problems/01-matrix/
'''


from collections import deque
class Solution:
	'''
	Brute force BFS solution. Iterate through every value in the array. If the value is nonzero, start
	a BFS from that location. Once the first zero is reached, assign the distance to the zero to
	the location in the matrix from which we started the search. Repeat for all non-zero values in the matrix.

	Time Complexity: O((m*n)^2), BFS O(m*n) from all m*n
	Space Complexity: O(m+n), the maximum size of our visited set
	'''
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
    	if not matrix or not matrix[0]:
    		return matrix
    	m, n = len(matrix), len(matrix[0])
    	dirs = [(1,0), (0,1), (-1,0), (0,-1)]
    	for i in range(m):
    		for j in range(n):
    			if matrix[i][j]:
    				queue = deque([((i,j),0)])
    				visited = set()
    				while queue:
    					pos, dist = queue.popleft()
    					if matrix[pos[0]][pos[1]] == 0:
    						matrix[i][j] = dist
    						break
    					for x, y in dirs:
    						new_pos = (new_x, new_y) = (pos[0] + x, pos[1] + y)
    						if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n and new_pos not in visited:
    							queue.append((new_pos, dist+1))
    							visited.add(new_pos)
    	return matrix


class Solution2:
	'''
	Dynamic programming solution. Let each cell represent the shortest distance from that cell to a 0.
	If we know the shortest distance of each of its four neighbors to a zero, the shortest distance to that cell is
	1 + min(shortest_neighbor). To apply this logic to a matrix, we need to do two sweeps: top-left to bottom-right
	and bottom-right to top-left. In the first pass, we initially set all nonzero cells to an arbitrarily large
	maximum value. 

	Time Complexity: O(m*n)
	Space Complexity: O(1)
	'''
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
		if not matrix or not matrix[0]:
			return matrix
		m, n = len(matrix), len(matrix[0])
		#Top-left to Bottom-right
		for i in range(m):
			for j in range(n):
				if matrix[i][j] != 0:
					#For first pass through, temporarily set the min distance of nonzero cells to arbitrarily large value
					matrix[i][j] = float('inf')
					if i > 0 and matrix[i-1][j] + 1 < matrix[i][j]:
						matrix[i][j] = matrix[i-1][j] + 1
					if j > 0 and matrix[i][j-1] + 1 < matrix[i][j]:
						matrix[i][j] = matrix[i][j-1] + 1

		for i in range(m-1,-1,-1):
			for j in range(n-1,-1,-1):
				if matrix[i][j] != 0:
					if i < m-1 and matrix[i+1][j] + 1 < matrix[i][j]:
						matrix[i][j] = matrix[i+1][j] + 1
					if j < n-1 and matrix[i][j+1] + 1 < matrix[i][j]
						matrix[i][j] = matrix[i][j-1] + 1
		return matrix
