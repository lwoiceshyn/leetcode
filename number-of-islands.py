'''

https://leetcode.com/problems/number-of-islands/

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

'''

class Solution:
    '''
    Note: Matrix values are strings, not ints, which caused me a lot of headache trying to use zero/nonzero boolean logic initially.

    We use an additional matrix to mark a cell on the grid as belonging to an island we have previously discovered. Iterate through
    each cell in the grid, and check if the cell is both a "1" on the grid and a "0" in the island matrix (undiscovered). If both 
    conditions are met, then perform a dfs to find all elements in the grid which are part of this island, and mark them on the 
    island matrix, and increase the island count by 1. Now, any subsequent element from this island will be skipped since it has
    already been marked on the island matrix. Each time we find a new undiscovered island, populate its corresponding elements
    in islands, and increase the island counter by 1, until we've checked every element in grid.

    Time Complexity: O(n*m*4^(n+m))
    Space Complexity: O(n*m)
    '''
    def __init__(self):
        self.dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    def dfs(self, grid, islands, i, j):
        islands[i][j] = "1"
        for a,b in self.dirs:
            x, y = i+a, j+b
            if x >= 0 and x <= len(grid)-1 and y >= 0 and y <= len(grid[0])-1 and grid[x][y] == "1" and islands[x][y] == "0":
                self.dfs(grid, islands, x, y)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        island_count = 0
        islands = [["0" for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and islands[i][j] == "0":
                    self.dfs(grid, islands, i, j)
                    island_count += 1

        return island_count


class Solution2:
    '''
    Same as above but we don't actually need an additional matrix, and can just change the island elements
    in the original matrix, leading to constant space complexity.

    Time Complexity: O(n*m*4^(n+m))
    Space Complexity: O(1)
    '''
    def __init__(self):
        self.dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    def dfs(self, grid, i, j):
        grid[i][j] = "#"
        for a,b in self.dirs:
            x, y = i+a, j+b
            if x >= 0 and x <= len(grid)-1 and y >= 0 and y <= len(grid[0])-1 and grid[x][y] == "1":
                self.dfs(grid, islands, x, y)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        island_count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    island_count += 1

        return island_count