'''
https://leetcode.com/problems/word-search/
'''


class Solution:
	'''
	Go through all cells, and at each cell run depth-first search, checking to see if the word
	is found from a path starting at that cell. DFS will check all possible paths from that cell
	so a solution is guaranteed to be found if it exists.

	In the DFS algorithm, the base cases area as follows: True, if the word passed in is an empty string, in which
	case we successfully found the word. False, if we tried searching outside of the board, or the cell we tried 
	searching in is not the next letter that we're looking for. In order to avoid backtracking and finding solutions
	where we went back to the starting cell, we temporarily set the cell that we are originating from to a '#' character,
	then recursively search all 4 adjacent cells, and then finally set this cell back to its original value once the
	DFS from this cell has concluded.

	Time Complexity: O(m*n*(3^s)), where s is the length of word. 3 since we're preventing backtracking.
	Space Complexity: O(s), since this is the maximum depth of the recursion tree.
	'''
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, word):
        if len(word) == 0:
            return True
        if i < 0 or i > len(board)-1 or j < 0 or j > len(board[0])-1 or word[0] != board[i][j]:
            return False

        tmp = board[i][j]
        board[i][j] = '#'

        found = self.dfs(board,i+1,j,word[1:]) or self.dfs(board,i-1,j,word[1:]) or \
                self.dfs(board,i,j+1, word[1:]) or self.dfs(board,i,j-1, word[1:])
        board[i][j] = tmp
        return found