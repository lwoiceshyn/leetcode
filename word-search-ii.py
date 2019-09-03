'''

https://leetcode.com/problems/word-search-ii/

'''
class Trie:
	'''
	Uses a nested dictionary structure to represent the trie. If a sequence of characters
	is considered a word, we use an additional end token in that level of the dictionary
	to represent that. 

	For insertion, simply iterate through the characters in the word sequentially. If that
	character is already a key, then simply move to the next level of the dictionary by going
	to the nested dictionary at that letter. If not, create a new empty dictionary at that letter.
	At the end of the word, add in an end token at that level.

	For search, simply go through each character sequentially, check if it's in the dictionary. If so,
	proceed to the next level by moving to the next nested dictionary. If not, then return False. If
	we got through the entire word successfully, then check for the end token. If it exists, return True,
	and if not, return False.
	'''
    def __init__(self):
        self.trie = {}

    def insert(self, word):
        current_dict = self.trie
        for c in word:
        	if c in current_dict:
        		current_dict = current_dict[c]
        	else:
        		current_dict[c] = {}
        		current_dict = current_dict[c]
        current_dict['end'] = ''


    def search(self, word):
        current_dict = self.trie
        for c in word:
        	if c in current_dict:
        		current_dict = current_dict[c]
        	else:
        		return False
        if 'end' in current_dict:
        	return True
        else:
        	return False
        
class Solution:
	'''
	The brute force solution would be to iterate through every element on the board, and then search for each
	word in the word list, if we haven't found that word yet, starting from that element. However, if we use
	a trie to represent our word list, we can simultaneously search for all of the words, while avoiding computational
	redundancy if words that we are searching for share the same prefix.

	First, initialize an empty trie as well as a set to store the found words it. When the function is called, build the
	trie with the words, then iterate through every element on the board. From each element, call a DFS function, which will
	add a found word to the class variable result, if found.

	For the DFS function, pass in the coordinates, the current node of the trie that we are in, and the current prefix
	represented by the node of the trie we are in. If the coordinates are a valid element on the board, check to see
	if the character at the current tile is child of the current trie node. If such, temporarily assign the board's 
	current element to a dummy character to avoid using it again in the search, and then call the function recursively
	four times for the four adjacent tiles, while advancing the trie to the subsequent node, and appending the character
	to the prefix we are carrying. If at any call, the 'end' token exists in the current trie node, we know we have
	found one of the desired words, so add it to the solution set.

	Time Complexity: O(m*n*(4^s)*w), where s is the word length, and w is the number of words.
	Space Complexity: O(s*w), w words of length s, which is the worst case space complexity of a trie.
	'''
    def __init__(self):
        self.result = set()
        self.root = Trie()
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for word in words:
            self.root.insert(word)
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):  
                self.dfs(self.root.trie, board, i, j)
        return list(self.result)

    def dfs(self, node, board, x, y, word=''):
        if 'end' in node:
            self.result.add(word)
        if (0 <= x <= len(board)-1) and (0 <= y <= len(board[0])-1):
            c = board[x][y]
            if c in node:
                word += c
                board[x][y] = '#'
                self.dfs(node[c], board, x+1, y, word)
                self.dfs(node[c], board, x-1, y, word)
                self.dfs(node[c], board, x, y+1, word)
                self.dfs(node[c], board, x, y-1, word)
                board[x][y] = c