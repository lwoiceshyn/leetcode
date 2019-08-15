'''

https://leetcode.com/problems/longest-substring-without-repeating-characters/

'''

class Solution:
	'''
	All we need to keep track of as we iterate through the string is the substring ending at the current index with no repeating characters in it.
	We can use a variable that keeps track of the longest substring without repeating characters we've seen so far, and once done iterating, will
	contain the length of the global overall substring without repeating characters. When we encounter a character that we've already seen before,
	our current substring ending on the index we are at will become the substring starting at the first character after the character we've already
	seen before. 

	We keep track of characters we've already seen before using a set, and we keep track of our current longest substring with no repeating characters
	with a moving window. The end of this moving window is simply the element of the string which we are currently at. The start of the window initially
	points to the start of the string, and when we encounter a repeated character, gets shifted forward to one position after the earlier instance of that
	repeated character. When we do this shift, we remove all of the characters from our set which came before it, i.e., characters that are no longer in
	our current moving window. Each time we add a new character, we update the max_window length that we've seen so far by comparing it to the current window
	length, and finally return max_window.

	Time Complexity: O(n)
	Space Complexity: O(d), where d is the length of the longest substring without repeating characters.
	'''
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        start = max_window = 0
        seen = set()
        for i, c in enumerate(s):
            if c not in seen:
                seen.add(c)
                new_window = i - start + 1
                max_window = max(new_window, max_window)
            else:
                while s[start] != c:
                    seen.remove(s[start])
                    start += 1
                start += 1
                
        return max_window