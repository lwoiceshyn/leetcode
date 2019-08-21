'''
https://leetcode.com/problems/valid-palindrome/

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''
class Solution:
	'''
	Use two pointers at the start and end to ensure that the characters match eachother. First check if the character is non-alphanumeric,
	in which case we don't care about it (commas, apostrophes, etc.), and advance each pointer to the next alphanumeric character. Then,
	check if the two characters match. If so, move each pointer inwards by 1. If not, return False. If the string either has an even or
	odd number of alphanumeric characters, the pointers will either end up on the same index, or past eachother by 1, and in either of 
	these cases, the while loop will break, all character pairs will have been checked, and the string is confirmed to be a palindrome.

	Time Complexity: O(n)
	Space Complexity: O(1)
	'''
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True

class Solution:
	'''
	A solution that trades off space complexity for elegance. Since a palindrome is the same after being reversed,
	simply grab all of the alphanumeric characters into a list and lowercase them. Then reverse the list (which is O(n))
	and check if the reversed version matches.

	Time Complexity: O(n)
	Space Complexity: O(n)
	'''
    def isPalindrome(self, s: str) -> bool:
        just_alnum = [c.lower() for c in s if c.isalnum()]
        return just_alnum == just_alnum[::-1]