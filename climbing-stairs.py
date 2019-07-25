'''
https://leetcode.com/problems/climbing-stairs/
'''

class Solution(object):
	'''
	The recurrence formula for this problem is simple.
	f(n) = f(n-1) + f(n-2), with the base cases of f(1) = 1 and f(2) = 2, since there is only one way to get to step one from the bottom, 
	and there are two ways to get to step two.

	This is the top-down approach, using a memoization table to store values that we have already calculated. Since our base cases are already 
	initialized in the table, we are already implicitly checking for them with our if statement, since they will always already exist as keys
	in memo. If we haven't reached the base case and we haven't stored a value in memo for a certain n yet, then store that value. Then,
	simply return memo[n].

	Time Complexity: O(n)
	Space Complexity: O(n)
	'''
    def __init__(self):
        self.memo = {1:1, 2:2}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n not in self.memo:
            self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
       	return self.memo[n]


class Solution2(object):
	'''
	This is the naive bottom-up approach. Simply create an array of length n, populate the first two values(base cases), then
	iterate through using the recursive formula, and return the value at the last index.

	Time Complexity: O(n)
	Space Complexity: O(n)
	'''
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
        	return 1
        arr = [0] * len(n)
        arr[0], arr[1] = 1, 2
        for i in range(2,n):
        	arr[i] = arr[i-1] + arr[i-2]
        return arr[n-1]

class Solution3(object):
	'''
	This is the optimized bottom-up approach. Once we've calculated the the number of ways to get to step n, we only need
	our previous value at n-1 and the value we just calculate to get our value at n+1, so we don't actually need to store 
	all of the past information in memory. Instead, we use two variables, initialized at the two base case value. At every 
	step of the iteration, we first set a temp variable equal to the variabl eat the last timestep. Then, we calculate the new 
	value at the current timestep and assign it to the second variable. Then, we simply set the old value to the temp variable,
	since in the next iteration this is now the number of ways to get to the timestep before last.

	Time Complexity: O(n)
	Space Complexity: O(1)
	'''
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
        	return 1
        x, y = 1, 2
        for i in range(2,n):
        	temp = y
        	y = x + y
        	x = temp
        return arr[n-1]