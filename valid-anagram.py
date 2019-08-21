'''

https://leetcode.com/problems/valid-anagram/

'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    	'''
    	All we need to do to verify if strings are anagrams of eachother is to see if they have the same number
    	of counts of characters. Assuming each string will have only lowercase characters, we can represent the
    	character counts of each string using a fixed-size list of length 29. Then, we simply iterate once through
    	the two strings, and use Python's ord function to convert the characters to their ascii integer value, but
    	subtract ord('a') from them so that 'a' will be 0 and 'z' will be 29, and then increment this value in
    	each of the two lists representing the character counts. Finally, return True if the two lists are equal,
    	False if not.

    	Time Complexity: O(n)
    	Space Complexity: O(1)


    	Follow-up: What if the characters are unicode?
    	Then use a dictionary to store the counts and compare dictionaries at the end, which will be O(n) space complexity.
    	'''
        if len(s) != len(t):
            return False
        char_counts_s = [0] * 29
        char_counts_t = [0] * 29
        for i in range(len(s)):
            char_counts_s[ord(s[i]) - ord('a')] += 1
            char_counts_t[ord(t[i]) - ord('a')] += 1
        return char_counts_s == char_counts_t


