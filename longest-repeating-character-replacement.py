'''
https://leetcode.com/problems/longest-repeating-character-replacement/

'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        This problem is solved using a sliding window. In order for our sliding window to contain a valid substring, it needs to meet a condition. For any
        given sliding window, we can keep track of the character counts of each character in that sliding window, and more importantly, keep track of the
        maximum of these counts. Then, if we look at the length of the window, and subtract the maximum character count from the length, we get the number
        of characters that we would need to replace for all of the characters in that window to be the same, e.g., our number of replacements needed. Then
        we can compare this to k, our allowed number of replacements, and if it's bigger than k, we need to decrease the window to make it valid.

        Thus, our constraint is len(window) - max_count <= k for the window to be a valid consideration. 

        We use a dictionary with keys as characters in the alphabet and values as their counts in the current sliding window, and keep track of the max window 
        length we have found so far for a valid window, max_window, as well as start, the start of the sliding window. The end of the sliding window will implicitly
        be the index of our enumerate loop. Then, each iteration, we increase the count of the character by 1, and update our max_counts variable. Then, we see
        if the current sliding window meets the constraint by comparing its length minus max_count to k, which we assign to the variable replacements_needed.
        If replacements_needed is greater than k, increment our start pointer by one, and subtract a character count from the character we just left out of the window.
        Continue this loop until we've reached a valid window. Then, update our max_window by comparing it to the length of the current max_window, and finally,
        return the highest max_window that we found.
        '''
        if not s:
            return 0
        alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()
        char_counts = {c:0 for c in alphabet}
        max_window = 0
        start = 0
        for i, c in enumerate(s):
            char_counts[c] += 1
            max_count = max(char_counts.values())
            replacements_needed = i - start + 1 - max_count
	        while replacements_needed > k:
	            char_counts[s[start]] -= 1
	            start += 1
	            replacements_needed = i - start + 1 - max_count
            max_window = max(max_window, i - start + 1)
        return max_window

