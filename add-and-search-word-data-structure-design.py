'''
https://leetcode.com/problems/add-and-search-word-data-structure-design/
'''

class WordDictionary:
	'''
	Use a trie to represent all of the words that the the data structure contains, with the trie being
	represented by a dictionary of nested dictionaries. 

	For insertion, simply iterate through the characters in the word sequentially. If that
	character is already a key, then simply move to the next level of the dictionary by going
	to the nested dictionary at that letter. If not, create a new empty dictionary at that letter.
	At the end of the word, add in an end token at that level.

	In order to be able to search for any regular expression string where a period represents any
	possible character, we need to perform a recursive depth-first traversal through the trie. The 
	base case is such that we are calling the DFS function on an empty string. In this scenario,
	if the end token is in the current dictionary level we are at, we know that we've successfully
	found the word. 

	We use a class variable to store the status of our search to simplify things and not have to pass
	an extra argument through every recursive function call. If we reach the successful version of
	the base case at any point in the traversal, set the variable to True.

	During the traversal, if the current character is a period, then call the function recursively
	on all child characters of that node. Otherwise, if the current character is a child of the current
	node, call the function recursively on that node and the rest of the word we're searching for. If
	the current character is not a child of our node, then we've reached a dead end, so return nothing.
	'''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        current_dict = self.trie
        for c in word:
        	if c in current_dict:
        		current_dict = current_dict[c]
        	else:
        		current_dict[c] = {}
        		current_dict = current_dict[c]
        current_dict['_end'] = {}
        

    def search(self, word: str) -> bool:
        """
        Returns True if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        self.contains = False
        self.dfs(self.trie, word)
        return self.contains

    def dfs(self, node, word):
        if not word:
            if '_end' in node:
                self.contains = True
            return
        if word[0] == '.':
            for c in node:
                self.dfs(node[c], word[1:])
        elif word[0] in node:
            self.dfs(node[word[0]], word[1:])
        else:
            return



class WordDictionary2:
    '''
    Same as above but without using a class variable to track if the word is found, 
    and instead having the recursive function call return True or False if the word is found.
    '''
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        temp = self.trie
        for c in word:
            if c not in temp:
                temp[c] = {}
            temp = temp[c]
        temp['_end'] = {}

    def search(self, word: str) -> bool:
        if not word:
            return False
        return self.dfs(word, self.trie)

    def dfs(self, word, level):
        if not word: 
            if '_end' in level:
                return True
            else:
                return False
        if word[0] != '.':
            if word[0] in level:
                return self.dfs(word[1:], level[word[0]])
            else:
                return False
        else:
            for char in level.keys():
                if self.dfs(word[1:], level[char]):
                    return True
            return False
