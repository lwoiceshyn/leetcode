'''

https://leetcode.com/problems/pacific-atlantic-water-flow/

'''


class Solution:
	'''
	The most efficient way to do the problem is in reverse. Have a separate visited matrix for the pacific and
	the atlantic, and then only perform DFS from cells in the pacific and atlantic portions of the matrix. Since
	we are going in reverse, we now need to check if the cell we are visiting is >= than the previous cell, rather than
	<=. Simply perform a DFS from each pacific cell using the pacific visited matrix, and from each atlantic cell using
	the atlantic visited matrix. Then, iterate once through each index, check if both atlantic and pacific are True for
	that index, and if so, append it to the results.

	Time Complexity:  O((m+n)*4^(m+n))
	Space Complexity: O(m*n)
	'''
    def __init__(self):
        self.dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def dfs(self, matrix, visited, i, j, prev=float('-inf')):
        if i >= 0 and i <= len(matrix)-1 and j >=0 and j <= len(matrix[0])-1 and matrix[i][j] >= prev and not visited[i][j]:
            visited[i][j] = True
            for x, y in self.dirs:
                self.dfs(matrix, visited, i+x, j+y, prev=matrix[i][j])

    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        res = []
        a_visited = [[False for _ in range(n)] for _ in range(m)]
        p_visited = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            self.dfs(matrix, p_visited, i, 0)
            self.dfs(matrix, a_visited, i, n-1)
        for j in range(n):
            self.dfs(matrix, p_visited, 0, j)
            self.dfs(matrix, a_visited, m-1, j)

        for i in range(m):
            for j in range(n):
                if a_visited[i][j] and p_visited[i][j]:
                    res.append([i,j])
        return res




class Solution2:
	'''
	My first attempt. Inefficient version where we run DFS from every single cell, and use a new visited matrix for each cell. Then check 
	if there is at least one visited True entry in both the atlantic and pacific sections. TLEs on Leetcode.

	Time Complexity: O(m*n*4^(m+n))
	Space Complexity: O(m*n)
	'''
    def dfs(self, matrix, visited, res, i, j, prev=float('inf')):
        if 0 <= i and i <= len(matrix)-1 and j >= 0 and j <= len(matrix[0])-1 and not visited[i][j]:
            if matrix[i][j] <= prev:
                if [i,j] in res:
                    return True
                visited[i][j] = True
                if i == 0 and j == len(matrix[0])-1:
                    return True
                if j == 0 and i == len(matrix)-1:
                    return True
                return self.dfs(matrix, visited, res, i+1, j, prev=matrix[i][j]) or self.dfs(matrix, visited, res, i-1, j, prev=matrix[i][j]) or \
                       self.dfs(matrix, visited, res, i, j+1, prev=matrix[i][j]) or self.dfs(matrix, visited, res, i, j-1, prev=matrix[i][j]) 

            else:
                return False
        else:
            return False


    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        res = []
        res.append([0,n])
        res.append([m,0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == len(matrix[0])-1:
                    continue
                elif j == 0 and i == len(matrix)-1:
                    continue
                else:
                    visited = [[False for _ in range(n)] for _ in range(m)]
                    if self.dfs(matrix, visited, res, i,j):
                        res.append([i,j])
                    else:
                        pacific = [visited[x][0] for x in range(0,m-1)]  + [visited[0][y] for y in range(1,n-1)]
                        atlantic = [visited[m-1][y] for y in range(1,n)] + [visited[x][n-1] for x in range(1,m-1)]
                        if any(pacific) and any(atlantic):
                            res.append([i,j])
        return res


