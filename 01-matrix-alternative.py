'''
Given a grid, of 'X', 'Y', and '0', find the shortest distance between any X and Y.

Example 1:

Input:
[[X,0,0],
 [0,Y,0],
 [X,Y,0]] 
Output: 1

Example 2:
Input:
[[X,X,0],
 [0,0,Y],
 [Y,0,0]] 
Output: 2
'''
grid = [['X', '0', '0'], 
        ['X', '0', '0'], 
        ['0', 'Y', 'Y']]


from collections import deque
class Solution:
	'''
	Since all we care about is the shortest distance between any X-Y pair in the grid, we can
	do a simultaneous BFS from every X. As soon as any search encounters Y, then we know that this
	is the closest possible Y to any X.

	Time Complexity: O(m*n * Number_Xs)
	Space Complexity: O(m*n)
	'''
	def shortest_pair(self, grid):
		m, n = len(grid), len(grid[0])
		dirs = [(1,0), (0,1), (-1,0), (0,-1)]
		queue = deque()
		visited = set()
		for i in range(m):
			for j in range(n):
				if grid[i][j] == 'X':
					queue.append((i,j), 0)
					visited.add((i,j))

		while queue:
			pos, dist = queue.popleft()
			if grid[pos[0]][pos[1]] == 'Y':
				return dist
			for x, y in dirs:
				new_x, new_y = pos[0] + x, pos[1] + y
				if new_x > 0 and new_x < m and new_y > 0 and new_y < n and (new_x, new_y) not in visited:
					queue.append((new_x, new_y), dist+1)
					visited.add((new_x, new_y))
		return -1

class Solution:
	'''
	DP solution. Min distance from an X-tile to any non-X-tile is 1 + the minimum
	distance to any of its four neighbors. Fill in the DP array in two passes: first, 
	go from top left to bottom right, and then from the bottom right to top left.

	Time Complexity: O(m*n)
	Space Complexty: O(m*n)
	'''
	def shortest_pair(self, grid):
		m, n = len(grid), len(grid[0])
		dp = [[float('inf') for _ in range n] for _ in range(m)]
		for i in range(m):
			for j in range(n):
				if grid[i][j] == 'X':
					dp[i][j] == 0
				else:
					if i > 0 and dp[i-1][j] + 1 <  dp[i][j]:
						dp[i][j] = dp[i-1][j] + 1
					if j > 0 and dp[i][j-1] + 1 < dp[i][j]:
						dp[i][j] = dp[i][j-1]

		for i in range(m-1,-1,-1):
			for j in range(n-1,-1,-1):
				if i < m-1 and dp[i+1][j] + 1 <  dp[i][j]:
					dp[i][j] = dp[i+1][j] + 1
				if j < n-1 and dp[i][j+1] + 1 < dp[i][j]:
					dp[i][j] = dp[i][j+1]

		min_dist = 0:
		for i in range(m):
			for j in range(n):
				if grid[i][j] == 'Y':
					min_dist = min(min_dist, dp[i][j])
		return min_dist
		






