'''
https://leetcode.com/problems/implement-trie-prefix-tree/
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

	For startsWith, do the same as above, but no need to check for an end token at the end, since we only
	care if it's a prefix or not.
	'''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current_dict = self.trie
        for c in word:
        	if c in current_dict:
        		current_dict = current_dict[c]
        	else:
        		current_dict[c] = {}
        		current_dict = current_dict[c]
        current_dict['_end'] = None


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current_dict = self.trie
        for c in word:
        	if c in current_dict:
        		current_dict = current_dict[c]
        	else:
        		return False
        if '_end' in current_dict:
        	return True
        else:
        	return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
    	for c in word:
        	if c in current_dict:
        		current_dict = current_dict[c]
        	else:
        		return False
       	return True
        
