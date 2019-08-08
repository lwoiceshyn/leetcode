'''
https://leetcode.com/problems/unique-paths/
'''

class Solution:
	'''
	Top-down dynamic programming (recursion + memoization). Every time we move down or right, we are solving a subproblem of the same type,
	just on a slighty smaller grid (optimal substructure property). Thus, we have a recursion tree with two children from each node,
	one for the subproblem where we move down, and one for the subproblem where we move right. First, we simply need to check for two
	base cases. One in which our movement took us off the grid, which is not a valid path. In this case, m or n becomes zero, and we
	return 0. The other base case is one in which we reached the final tile, where m and n are both 1. In this case, we return 1.

	Otherwise, call the function recursively on both subproblems, in which we just need to subtract one for either argument,
	and then sum up the values that they return, which indicate how many valid paths can be reached from that branch. 

	We use a memoization table to ensure that we don't recalculate overlapping subproblems.
	
	We use a nested list for our memo table and a separate function for the recursion so that we can initialize it. Also,
	need to make the dimensions m+1 x n+1 so that when we call memo[m][n] we are still in-bounds, due to zero-indexing.

	Time Complexity: O(n^2)
	Space Complexity: O(n^2)
	'''
    def uniquePaths(self, m: int, n: int) -> int:
        self.memo = [[0 for _ in range(n+1)] for _ in range(m+1)] #Note that the second index is the inner index
        return self.recurse(m, n)
    def recurse(self, m, n):
        if m == 0 or n == 0:
            return 0
        if m == 1 and n == 1:
            return 1
        if not self.memo[m][n]:
            right = self.recurse(m-1, n)
            down = self.recurse(m, n-1)
            self.memo[m][n] = right + down
    
        return self.memo[m][n]

class Solution2:
	'''
	Bottom-up dynamic programming solution. We will use a 2D m x n DP array, in which the value at each index signifies the
	number of valid paths that end at that tile, with the starting tile having a initial value of 1. Then, we simply iterate through
	all the tiles, adding the number of valid paths from the tile above and the tile to the left of the current tile, with an if
	statement to handle the case where we are in the top row or left column of the grid, ensuring we don't try to index outside of
	our array.  

	Time Complexity: O(n^2)
	Space Complexity: O(n^2)
	'''
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)] 
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
        return dp[m-1][n-1]
