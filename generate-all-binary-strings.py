'''
https://www.tutorialcup.com/string/generate-binary-strings-given-pattern.htm
'''

from collections import deque
class Solution:
	'''
	Use a queue, simply add both possibilities to the queue whenever 
	there's a question mark character, and keep track of the index to
	resolve the next letter to add to the string. 

	Time Complexity: O(2^Num_question_marks)
	Space Complexity: O(2^Num_question_marks)
	'''
	def generate_strings(self, s):
		res  = []
		queue = deque([('', 0)])
		while queue:
			curr_str, idx = queue.popleft()
			if idx == len(s):
				res.append(curr_str)
				continue
			next_char = s[idx]
			if next_char = '?':
				queue.append((curr_str + '0', idx+1))
				queue.append((curr_str + '1', idx+1))
			else:
				queue.append((curr_str + next_char, idx+1))
		return res



class Solution2:
	'''
	Recursive solution, basically the same as the iterative but 
	using a recursive nested function that gets called twice recursively
	whenever a '?' counter is encountered.

	Time Complexity: O(2^Num_question_marks)
	Space Complexity: O(2^Num_question_marks)
	'''
	def generate_strings(self, s):
		res = []
		def helper(item, idx):
			if idx == len(s):
				res.append(item)
				return
			next_char = s[idx]
			if next_char == '?':
				helper(item+'0', idx+1)
				helper(item+'1', idx+1)
			else:
				helper(item+next_char, idx+1)
		helper('', 0)
		return res