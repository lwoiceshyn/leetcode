'''

https://leetcode.com/problems/group-anagrams/

'''

class Solution:
	'''
	For two strings to be an anagram of eachother, they need to have the same count of characters. We can use a helper function
	to get the character count for a string in linear time and constant space complexity, and return a tuple of the character counts,
	so that we have a hashable representation. Then, go through the list of strings, and use the function to return its character counts
	tuple. Use this as a dictionary key, and if it's already a key, append it to the list there, and if not, start a new list with this 
	key. Then simply return the dictionary values, which will be a list of lists.

	Time Complexity: O(n*m), where n is the number of strings, and m is the length of the longest string.
	Space Complexity: O(n*m), where n is the number of strings, and m is the length of the longest string.
	'''
    def charCounts(self, s):
        char_counts = [0] * 29
        for c in s:
            char_counts[ord(c) - ord('a')] += 1
        return tuple(char_counts)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        groups = {}
        for string in strs:
            char_counts = self.charCounts(string)
            groups[char_counts] = groups.get(char_counts, []) + [string]
        return list(groups.values())

class Solution2:
	'''
	Same as above, but instead of using character counts, simple take a tuple of the sorted string. Note that sorting an ascii string
	can be linear time complexity using certain algorithms (https://en.wikipedia.org/wiki/Counting_sort).

	Time Complexity: O(n*m), where n is the number of strings, and m is the length of the longest string.
	Space Complexity: O(n*m), where n is the number of strings, and m is the length of the longest string.
	'''
	def groupAnagrams(self, strs):
	    groups = {}
	    for s in strs:
	        key = tuple(sorted(s)) 
	        groups[key] = groups.get(key, []) + [s]
	    return list(groups.values())
