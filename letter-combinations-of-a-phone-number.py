'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''


from collections import deque, defaultdict
class Solution:
    '''
    Simple BFS using a queue. Pop the next queue element out, if its idx is the same as the length
    of the input string, then we've reached a solution, so append it. Otherwise, go through all of
    the possible characters mapped to that digit and append a version of the current string + each
    character to the queue.
    '''
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        queue = deque([("", 0)])
        res = []
        mapping = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        while queue:
            curr_str, idx = queue.popleft()
            if idx == len(digits):
                res.append(curr_str)
                continue
            next_digit = digits[idx]
            for c in mapping[next_digit]:
                queue.append((curr_str + c, idx+1))
        return res
        