'''
https://leetcode.com/problems/generate-parentheses/
'''


class Solution:
	'''
	To build one solution string from scratch, we need to know how many open
	parentheses we have available, and how many unclosed parentheses are in the
	current string. For example, if n = 3, and the current string we're building
	already uses 3 open parentheses, we can't add any more and have a balanced solution.
	Likewise, if the current string we are building has no open parentheses, we can't add
	a closing parenthesis to it without breaking balance. 

	Recursively, our base case is having no open parentheses left. In this case, add as many 
	closed parentheses as we need to balance them. Otherwise, we have no unclosed parentheses,
	so we need to add a new open parenthesis. If neither of these is the case, we can add either
	an open or a closed parenthesis, so call the function recursively for both these paths down
	the solution set.

	Time Complexity: O(4^n / sqrt(n)), how this is derived is not really necessary, just know this is exponential.
	Space Complexity: O(4^n / sqrt(n))
	'''
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(curr, num_open, num_unclosed=0):
        	if num_open == 0:
        		return [curr + ')' * num_unclosed]
        	if num_unclosed == 0:
        		return helper(curr + '(', num_open-1, num_unclosed+1)
        	return helper(curr + '(', num_open-1, num_unclosed+1) + helper(curr + ')', num_open, num_unclosed-1)
        return helper("", n)


from collections import deque
class Solution2:
	'''
	Exacty same logic as above solution but done iteratively using a queue.
	'''
    def generateParenthesis(self, n: int) -> List[str]:
        queue = deque([('', n, 0)]) # (current string, num_open_left, num_unclosed)
        res = []
        while queue:
            curr_str, num_open, num_unclosed = queue.popleft()
            if len(curr_str) == 2 * n:
                res.append(curr_str)
                continue
            if num_open == 0:
                res.append(curr_str + ')' * num_unclosed)
                continue
            if num_unclosed == 0:
                queue.append((curr_str + '(', num_open-1, num_unclosed+1))
            else:
                queue.append((curr_str + '(', num_open-1, num_unclosed+1))
                queue.append((curr_str + ')', num_open, num_unclosed-1))
        return res
