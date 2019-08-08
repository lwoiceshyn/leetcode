'''
https://leetcode.com/problems/decode-ways/
'''

class Solution:
	'''
	Top-down dynamic programming solution using recursion + memoization. When considering valid ways to decode the input, we only care about either single 
	digits or pairs of sequential digits. Any single digit other than 0 can be validly decoded to a letter, but only double digits that are both less than
	27 and do not contain a first digit of 0 are valid. We want to build a recursion tree that progresses towards a base case, where there's either one digit 
	left to decode or zero digits left to decode. In these cases, we've reached the end of a recursion branch which was a valid decode, and thus we return 1.
	We have to also ensure that if there's only one digit, but that digit is zero, it is not a valid decode. Thus, we check if the first digit is zero,
	and if so, return 0, since this is a dead end that did not lead to a valid decode. At each node, we want to branch into the two cases, one in which we 
	consider the first digit as a single digit, and one in which we consider the first two digits as a pair. 

	In the first case, we simply call the function recursively on the rest of the string after the first digit. In the second case, we first check if the 
	number is greater than 26. If so, simply return whatever the value from the single-digit branch was, since the two-digit branch from this node is a dead end.
	Note that we already checked if the first digit was 0, which makes both branches from this node dead ends, and returned 0 in that case. If it's not greater than
	26, and thus valid, call the function recursively on the rest of the string after this two-digit pair, and then finally return the sum of the valid decodes from each
	of these branches.

	We use a memo dictionary to ensure we don't recalculate overlapping subproblems.

	Time Complexity: O(n)
	Space Complexity: O(n) (But fairly inefficient since were using the actual array as a key. Better version would use something like tracking the index into s)
	'''
    def __init__(self):
        self.memo = {}
    def numDecodings(self, s: str) -> int:
        if (len(s) == 1 or len(s) == 0) and s != "0": 
            return 1
        if s[0] == "0":
            return 0
        if s not in self.memo:
            first = self.numDecodings(s[1:])
            if int(s[:2]) > 26: 
                self.memo[s] = first
            else:
                second = self.numDecodings(s[2:])
                self.memo[s] = first + second
        return self.memo[s]


class Solution2:
	'''
	Bottom-up dynamic programming solution. We create a DP array, where each value at index i indicates the number of valid decodes that end at that index. 
	The recursive formulation: if s[i-1:i+1] is a valid two-digit number: dp[i] += dp[i-2] 
						       if s[i-1] is a valid single-digit number OR s[i-2:i] is a valid two-digit number: dp[i] += dp[i-1] 

	So overall, the formulation is similar to the Fibonacci sequence, but has the additional complications that need to be analyzed when considering if we
	are allowed to add the values, i.e., is there a valid path between i-1 and i, and is there a valid path between i-2 and i.

	Initializing the first two values of the array is also a bit tricky. The first value is simply either 1 if its a non-zero value, or 0 if not. In the
	case where it's 0, then there cannot be a valid path at all, since the first two-digit possibility also starts with 0, which isn't valid.

	The second value has a few different possibilities:
	a) The second digit is 0 and the first two values make a number less than 27 .In this case, set it to 1, since the only valid path to here is the two-digit number itself.
	b) The second digit is 0 and the first two values make a number greater than 26. In this case, set it to 0, since no valid paths exist to this location, as it ends in zero, 
	and the two-digit is invalid.
	c) The second digit is not 0 and the first two values make a number less than 27. In this case, set it to 2, since both the two-digit and double one-digit paths are valid.
	d) The second digit is not 0 and the first two values make a number greater than 26. In this case, set it to 1, since only the double one-digit path is valid.

	Then, we simply iterate through our DP array and use some logic to check valid paths: 

	If s[i-1:i+1], i.e., the two-digit number ending in the current slot, is valid (less than 27 and first digit non-zero), 
	then add dp[i-2], since this is a path that is going from s[i-2] using the two digit number s[i-1:i+1].

	In the other scenario, it is either a valid path from the two-digit number s[i-2:i], i.e., the two-digit number ending in the
	previous slot, plus the current single-digit value, or a valid path from the last single-digit to the current. We need to check if
	either of these is valid. If the current value is 0, then neither path is valid since the current single-digit value is not a valid 
	decode, so we first check for this. Then, we check if the prior digit is non-zero. In that case, then a path exists using the current single
	digit and the last single-digit and we can add the value from dp[i-1]. If it is zero, we can still have a valid path, if and only if, the
	prior two-digit number is valid, i.e., it is less than 27, and doesn't contain a leading 0 (so greater than 9). If this case is met,
	then proceed with adding dp[i-1].


	Time Complexity: O(n)
	Space Complexity: O(n) (This can easily be O(1) by just using temp variables since we only need to keep track of the two past values of the DP array)
	'''

	def numDecodings(self, s: str) -> int:
	    if len(s) == 0:
	        return 0
	    if len(s) == 1: 
	        if s != "0":
	            return 1
	        else:
	            return 0
	    dp = [0] * len(s)
	    if s[0] == "0":
	    	return 0
	    else:
	    	dp[0] = 1 
	   	if s[1] == "0":
	   		if int(s[0:2]) < 27:
	   			dp[1] = 1
	   		else:
	   			dp[1] = 0
	   	else:
	   		if int(s[0:2]) < 27:
	   			dp[1] = 2
	   		else:
	   			dp[1] = 1  
	    for i in range(2, len(dp)):
	        if int(s[i-1:i+1]) < 27 and s[i-1] != "0":
	            dp[i] += dp[i-2]
	        if s[i] != "0":
	            if s[i-1] != "0" or 9 < int(s[i-2:i]) < 27:
	                dp[i] += dp[i-1]
	    return dp[-1]