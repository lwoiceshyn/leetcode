'''
https://leetcode.com/problems/palindromic-substrings/

'''


class Solution:
	'''
	A valid palindrome is either of an even-length, or an odd-length. In the even-length case, the palindrome is centered on
	two of the same character, such as 'abba'. In the odd-length case, the palindrome is centered on any single character, 
	such as 'aba'. Thus, we can iterate through all of the characters in the string, and count how many odd-length palindromes
	are centered on that character, and how many even-length palindromes are centered on that character and the preceding 
	character. Then, we can sum these up for every character in the string to get the total number of palindromic substrings.

	In implementation, I use a count function that counts how many palindromes are centered from some starting point in a string.
	It uses two pointer values as parameters. For the odd-length case, these are set to the same value initially, and for the even
	length case, they will be one apart. Then, a while loop is used to check that if both pointers are still in valid locations of
	the string, and if the values they each point to are identical, then a valid palindrome exists, and each moves outward by 1,
	and a value of 1 is added to count. For the odd-length palindromes, there is automatically a valid palindrome of length 1
	that will be found for each character in the string, since initially, left = right and s[left] will automatically be equal
	to s[right].

	Time Complexity: O(n^2)
	Space Complexity: O(1)
	'''
    def countSubstrings(self, s: str) -> int:
    	even_counts = odd_counts = 0
   		for i in range(len(s)):
   			odd_counts += self.count(s,i,i)
   			even_counts += self.count(s,i-1,i)
   		return even_counts + odd_counts

   	def count(self, s, left, right):
   		count = 0
   		while left >= 0 and right < len(s) and s[left] == s[right]:
   			left -= 1
   			right += 1
   			count += 1
        return count                                                                                                               