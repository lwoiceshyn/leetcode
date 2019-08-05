'''
https://leetcode.com/problems/word-break/
'''


class Solution:
	'''
	Bottom-up solution. Create a DP array of len(s) + 1, with each element being a boolean value initialized to False, except the 
	initial value, which is initialized to True. Any element in the array at index i being True signifies that a prefix to that index
	was a word in the dictionary which ended at index i-1. 

	Then, iterate through the DP array, and at each iteration, check all possible
	prefixes to that index. If the prefix is a word in the dictionary, and the dp array's value at the first index of that prefix is True,
	indicating that a dictionary word ended on the index prior to it, then set dp of the current element to True, meaning that the prefix
	is both a dictionary word and is following a dictionary word.

	Finally, if the last value in DP has been set to True, we know that there is a path of dictionary words which perfectly breaks the string
	into segments which are all dictionary words.

	Time Complexity: O(n^2), could be O(n*max_word_length) if we optimize and only iterate through prefixes in the range of possible lengths.
	Space Complexity: O(n)
	'''
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[-1]

class Solution:
	'''
	Top-down solution. We follow a recursive formula such that if the current string has a prefix which is in the wordDict, then recurse on the remainder of the
	string. If not, then return False. If the length is zero, then return True, as we have found a branch which was able to break the entire string into words
	from wordDict. Note that at every stage we need to check all possible branches of the recursion tree, and not just the first prefix we find. That is why we
	use the check_prefix variable to see if True is returned from that branch, and if not, try the rest of the prefixes.

	A memoization dictionary is used to handle the overlapping subproblems.

	Time Complexity: O(n*max_word_length)
	Space Complexity: O(n)
	'''
    def __init__(self):
        self.memo = {}
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s or not wordDict:
            return False
        else:
            longest = len(max(wordDict, key=len))
            return self.recurse(s, wordDict, longest)
    def recurse(self, s, wordDict, longest):
        if len(s) == 0:
            return True
        if s not in self.memo:
            for i in range(longest+1):
                if s[:i] in wordDict:
                    check_prefix = self.recurse(s[i:], wordDict, longest)
                    if check_prefix:
                        self.memo[s] = True
                        return self.memo[s]
            self.memo[s] = False
        return self.memo[s]

