'''
Problem Link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

My initial solution (clunky). Checks adjacent characters for repetition, and if so, deletes them and goes back to previous index
to ensure that any newly created duplicates are covered.
'''

class Solution:
    def removeDuplicates(self, S: str) -> str:
        char_list = list(S)
        i = 0
        while True:
            if char_list[i+1] == char_list[i]:
                del char_list[i:i+2]
                i -= 1 
                if i < 0:
                    i = 0
            else:
                i += 1
            
            if i == len(char_list)-1 or len(char_list) == 0:
                break
        
        if len(char_list) == 0:
            return ''
        else: 
            return ''.join(char_list)   


'''
Optimal Solution. Uses an explicit stack (represented as a list) to store non-duplicate characters. If a duplicate is encountered, it just gets popped off the stack.
This method automatically handles new duplicates being created due to the stack having the last non-duplicate character at the end.
'''

class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for c in S:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)

'''
Complexity Analysis:
Time: O(n) where n is the length of the input string.
Space: O(n-d) where n is the length of the input string and d is the total length of all duplicate characters
'''