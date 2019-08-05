'''
https://www.hackerrank.com/challenges/dynamic-programming-classics-the-longest-common-subsequence/problem
'''


'''
The recursive formula for this problem is as follows. Define the two inputs as sequence a of length n, and sequence b of length m. 
There are three potential cases when examining these two sequences.

1) The sequences end in the same value.
2) The sequences end in a different value.
3) One of the two sequences is empty.

In the first case, the LCS is the simply the shared element plus the LCS of the two sequences minus their last element. LCS = LCS(a[1...n-1], b[1...m-1]) + a[-1]

In the second case, the LCS is either LCS(a[1...n-1], b[1...m]) or LCS(a[1...n], b[1...m-1]), whichever of these two sequences is longer.

The last case is the base case, in which the LCS of the two sequences is zero, since there is no intsersection.

The following is the top-down solution using recursion plus memoization. Since the problem on hackerrank is using a list of integers for some reason,
I use a helper function to map the sequences into strings so they are hashable and thus usable as keys for the memo dictionary.

Time Complexity: O(m*n)
Space Complexity: O(m*n)
'''

memo = {}
def strmap(a,b):
    return(''.join(map(str,a)), ''.join(map(str,b)))
def longestCommonSubsequence(a, b):

    if len(a) == 0 or len(b) == 0:
        return []
    if strmap(a,b) not in memo:
        if a[-1] == b[-1]:
            memo[strmap(a,b)] = longestCommonSubsequence(a[:-1], b[:-1]) + [a[-1]]
        else:
            x = longestCommonSubsequence(a[:-1],b)
            y = longestCommonSubsequence(a, b[:-1])
            if len(x) > len(y):
                memo[strmap(a,b)] = x
            else:
                memo[strmap(a,b)] = y
    return memo[strmap(a,b)]


