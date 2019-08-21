'''
https://leetcode.com/problems/minimum-window-substring/

'''

class Solution:
	'''
	My first attempt without any outside help. Passes tests but slow. We want to use a sliding window to represent our window which contains
	at least all the characters in T. I use a dictionary to track how many of each of the characters in T are currently in our window,
	and a dictionary called tracker_req which stores the counts of each character in t. A helper function called check_tracker will
	check if we have at least the minimum number of counts of each character in our sliding window so that the requirement is met. If met,
	then this is a valid sliding window. 

	We initialize a variable first_char, which tracks the first character in our sliding window, which will be a character in T, if that exists in S, 
	and start, which is a pointer to the first value of our sliding window. When we reach the first char in S that's also in T, set start to this
	value, and set first_char to this char. Then, we continue iterating, adding any char in T to our tracker, and keep checking to see if it
	meets the requirement of meeting all char counts in T. If that requirement is met, we have a valid window, and we check if it's smaller than
	the smallest we've seen so far, and if so, set our smallest window to that. 

	Then, we have a secondary check, which checks if the first_char is redundant, i.e., is the count of the number of first_char greater than
	the minimum required to make the window valid. If so, then increment our start pointer until it reaches the next char in T, and remove one
	from the counter of the previous first_char. Set the new first_char to s[start]. Do this check over and over until first_char is not
	redundant anymore. This ensures we will always find the smallest possible window, since multiple redundancies can occur when the first
	one occurs.

	Finally, once we've iterated over the entire string, return the string corresponding to the slice of S from the smallest window that we found.

	Time Complexity: O(s), maybe O(s*t)?
	Space Complexity: O(t)

	'''
    def check_tracker(self, tracker, tracker_req):
        for k in tracker.keys():
            if tracker[k] < tracker_req[k]:
                return False
        return True
    
    def minWindow(self, s: str, t: str) -> str:
        tracker = {c:0 for c in t}
        tracker_req = {c:t.count(c) for c in t}
        first_char = None
        start = 0
        min_window = len(s) + 1
        return_window = ""
        for i, c in enumerate(s):
            if c in tracker:
                tracker[c] += 1
                if not first_char:
                    start = i
                    first_char = c
            if self.check_tracker(tracker, tracker_req):
                if i-start+1 < min_window:       
                    min_window = i-start+1
                    return_window = s[start:i+1]
                while self.check_tracker(tracker, tracker_req) and tracker[first_char] > tracker_req[first_char] and start < i:
                    start +=1
                    tracker[first_char] -= 1
                    while start < i and s[start] not in tracker:
                        start +=1
                    if start < len(s):
                        first_char = s[start]
            if self.check_tracker(tracker, tracker_req):
                if i-start+1 < min_window:
                    min_window = i-start+1
                    return_window = s[start:i+1]   
        return return_window


class Solution2:
	'''
	Essentially the same logic as above but much more concise/efficient. The object need is a Counter object that keeps track of how many of a certain char we need for our
	window to be valid, while missing keeps track of how many more chars in T we need for to be valid. As we come across a new char, if need[char] > 0, which
	will initially only be chars in T, subtract 1 from missing. Reduce need[char] by 1. Then, if missing == 0, aka, we have a valid window, then go to our
	start pointer, and check if need[start] < 0, in which case start is not a pointer in T. Then increase start until need[start] == 0, which means we 
	are not redundant in the chars we need, and while we increment start, increase need for each char we leave behind by 1. Then, once this while
	loop breaks, we are in a situation where we have a non-redundant sliding window, and thus compare our previous best start and end indices with
	the current, and if the current ones form a smaller window, set the previous best ones to the current ones. Then return a slice at the end
	with the best start and end indices we found.

	Time Complexity: O(s)
	Space Complexity: O(s), since need will add all chars in s to it.

	'''
	def minWindow(self, s: str, t: str) -> str:
		import collections
	    need, missing = collections.Counter(t), len(t)
	    start = best_start = best_end = 0
	    for end, c in enumerate(s, 1):
	        missing -= need[c] > 0 
	        need[c] -= 1 
	        if not missing: 
	            while start < end and need[s[start]] < 0: 
	                need[s[start]] += 1 
	                i += 1 
	            if not best_end or end - start <= best_end - best_start: 
	                best_start, best_end = start, end
	    return s[best_start:best_end]