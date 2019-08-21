'''

https://leetcode.com/problems/valid-parentheses/

'''

class Solution:
	'''
	For the parentheses to be valid, each right parenthesis we see has to match the last left parenthesis we saw,
	and all left parentheses have to have a matched right parenthesis. Since we care about the last one we saw,
	we can use a stack to track the left parethenses. Then, once we reach a right parenthesis, compare it to the
	last left parenthesis in the stack. If it's a match, remove from the stack. If not, return False. Once we've
	gone through the entire string, if it is balanced, the stack should be empty. If so, return True, and if not,
	return false.

	Time Complexity: O(n)
	Space Complexity: O(n)
	'''
    def isValid(self, s: str) -> bool:
        d = {'(':')', '[':']', '{':'}'}
        stack = []
        for c in s:
            if c in d:
                stack.append(c)
            else:
                if stack:
                    last = stack.pop()
                    if d[last] != c:
                        return False
                else:
                    return False
        if not stack:
            return True
        else:
            return False