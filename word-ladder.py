'''
https://leetcode.com/problems/word-ladder/
'''

class Solution:
	'''
	Bidirectional breadth-first search solution. Bidirectional BFS at worst case performs as well as unidirectional BFS,
	but in cases where the start node has many more directions to explore than the end node, it can significantly improve
	run speed.

	First, create a front and back queue using sets, and set the steps variable to 1. Since the first word is considered
	part of the transformation sequence. Then, each iteration, we will go through all of the words in the current queue
	that we are processing, and populate a next_front queue that we will assign to the current front variable once we've 
	processed all words in front. For each word, try changing each letter to every other possible letter. If we found a word in
	the other queue by making this chance, return steps. Otherwise, check if it's in wordList. If so, add the word to 
	the next_queue, and remove that word from wordList, since we don't want to backtrack to already visited words.
	Once all of the current words have been processed, set front to next_front. Then, if back is shorter than front,
	swap the two queues so that we're now processing back.

	Time Complexity: O(V+E)
	Space Complexity: O(V+E)
	'''
	def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
	    if endWord not in wordList:
	        return 0
	    front = {beginWord}
	    back = {endWord}
	    steps = 1
	    wordList = set(wordList)
	    word_length = len(beginWord)
	    while front:
	        steps += 1
	        next_front = set()
	        for word in front:
	            for i in range(word_length):
	                for c in 'abcdefghijklmnopqrstuvwxyz':
	                    if c != word[i]:
	                        new_word = word[:i]+c+word[i+1:]
	                        if new_word in back:
	                            return steps
	                        if new_word in wordList:
	                            next_front.add(new_word)
	                            wordList.remove(new_word)
	        front = next_front
	        if len(back)<len(front):
	            front, back = back, front
	    return 0

from collections import deque, defaultdict
class Solution2:
	'''
	Unidirectional breadth-first search with preprocessing. Construct a hashmap that maps all
	of the words in wordList with one letter missing to all the words which can be found in the
	wordDict by filling in the missing letter. Then, use a queue and perform BFS, using a visited
	set to track if we've seen the word before. If we haven't, check if its the end word. If so,
	return steps. If not, go through each character in the current word, replace it with '_', and
	grab the words in the dictionary that it can map to in wordList, if they have not been visited yet,
	and append them to the queue, attached to steps+1.

	Time Complexity: O(V+E)
	Space Complexity: O(V+E)
	'''
    def ladderLength(self, beginWord, endWord, wordList):  
		def construct_dict(word_list):
			'''
			Creates a dictionary that maps all words in the word_list with one
			letter missing to all of the words in word_list that can be transformed
			with filling in that missing letter.
			'''
		    d = collections.defautdict(list)
		    for word in word_list:
		        for i in range(len(word)):
		            s = word[:i] + "_" + word[i+1:]
		            d[s].append(word)
		    return d
            
        def bfs_words(begin, end, dict_words):
            queue, visited = deque([(begin, 1)]), set()
            while queue:
                word, steps = queue.popleft()
                if word not in visited:
                    visited.add(word)
                    if word == end:
                        return steps
                    for i in range(len(word)):
                        s = word[:i] + "_" + word[i+1:]
                        neigh_words = dict_words.get(s, [])
                        for neigh in neigh_words:
                            if neigh not in visited:
                                queue.append((neigh, steps + 1))
            return 0
        
        d = construct_dict(wordList)
        return bfs_words(beginWord, endWord, d)

class Solution3:
	'''
	Unidirectional recursive depth-first search with cycle detection. TLE on Leetcode but solution at least works.

	Time Complexity: O(V+E)
	Space Complexity: O(V+E)
	'''
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        self.target = endWord
        self.wordList = wordList
        self.min_steps = float('inf')
        visiting = {word:False for word in wordList}
        visiting[beginWord] = False
        visiting[endWord] = False
        self.dfs(beginWord, visiting)
        return self.min_steps if self.min_steps < float('inf') else 0
    
    
    def dfs(self, word, visiting, step_count=1):
        if word == self.target:
            if step_count < self.min_steps:
                self.min_steps = step_count
        if visiting[word]:
            return
        visiting[word] = True
        for other_word in self.wordList: 
            if not visiting[other_word] and self.difference(word, other_word) == 1:
                self.dfs(other_word, visiting, step_count+1)
        visiting[word] = False

    def difference(self, a,b):
        diff_count = 0
        for c_a, c_b in zip(a,b):
            if c_a != c_b:
                diff_count += 1
        return diff_count

from collections import deque
class Solution4:
	'''
	Unidirectional breadth-first search. TLE on Leetcode but solution works.

	Time Complexity: O(V+E)
	Space Complexity: O(V+E)
	'''
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque([(beginWord, 1)])
        visited = set()
        while queue:
            word, count = queue.popleft()
            if word == endWord:
                return count
            visited.add(word)
            for other_word in [item for item in wordList if item not in visited]:
                if self.difference(word, other_word) == 1:
                    queue.append((other_word, count+1))
        return 0

    def difference(self, a,b):
        diff_count = 0
        for c_a, c_b in zip(a,b):
            if c_a != c_b:
                diff_count += 1
        return diff_count




