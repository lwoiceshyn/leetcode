'''
https://leetcode.com/problems/n-queens/
'''


class Solution:
    '''
    Backtracking solution. First, make a n x n grid to store queen positions on for checking.
    The is_safe function takes a position on the grid and checks to see if any prior element on
    the same row has a collision, any prior element on the top diagonal has a collision, and
    any prior element on the bottom diagonal has any collision.

    The build_res function takes the grid and returns a solution in the required format by finding
    the positions of the queens in the grid.

    For the recursive n_queens function, iterate through each column at a time. Search for an empty
    location in the column with no collisions to place a queen, and then call the function on the
    next column recursively. If we hit the base case, col >= n , then append a solution to our
    results list by calling build_res. Otherwise, set the value of the current element back to 
    zero and backtrack by first trying other locations in the column, and if no other potential solutions, 
    backtracking to the previous column.

    Time Complexity: O(n!)
    Space Complexity: O(n^2)
    '''
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [[0 for _ in range(n)] for _ in range(n)]
        res = []
        def is_safe(grid, x, y):
            for j in range(y):
                if grid[x][j]:
                    return False
            i, j = x-1, y-1
            while i >= 0 and j >= 0:
                if grid[i][j]:
                    return False
                i -= 1
                j -= 1
            i, j = x+1, y-1
            while i < n and j >= 0:
                if grid[i][j]:
                    return False
                i += 1
                j -= 1
            return True    
        
        def build_res(grid, n):
            ret = [['.' for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    if grid[i][j]:
                        ret[i][j] = 'Q'
            return [''.join(row) for row in ret]
                    
        def n_queens(grid, col, n, res):
            if col >= n:
                return True
            for i in range(n):
                if is_safe(grid, i, col):
                    grid[i][col] = 1
                    if n_queens(grid, col+1, n, res):
                        res.append(build_res(grid, n))
                    grid[i][col] = 0
        n_queens(grid, 0 , n, res)
        return res


class Solution2:
    '''
    More space efficient backtracking solution (credit caikehe on Leetcode).

    Represent our board as a single 1-D array where index is row and element is column. Iterate 
    through the rows, and use an index variable to track which row we are on. Try placing a queen
    in each column and check if that placement is valid. If so, call the function recursively.
    Repeat this until we find a solution (base case index == len(array)). or until we explore
    all possible solution paths.

    Time Complexity: O(n!)
    Space Complexity: O(n)
    '''
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        self.dfs([-1]*n, 0, [], res)

    def dfs(self, nums, index, curr_res, res):
        if index == len(nums):
            res.append(curr_res)
            return
        for i in range(nums):
            nums[index] = i
            if self.is_safe(nums, i):
                tmp = '.' * len(nums)
                self.dfs(nums, index+1, curr_res + [tmp[:i] + 'Q' + tmp[i+1:]], res)

    def is_safe(self, nums, n):
        '''
        For two coordinates to be diagonal to eachother, they form a square,
        and the difference between x and y coordinates must therefore be the same.

        Also, a queen cannot be in a previous column.
        '''
        for i in range(n):
            if abs(nums[i]-nums[n]) == n-i or nums[i] == nums[n]:
                return False
        return True
