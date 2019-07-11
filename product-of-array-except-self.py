'''
Problem Link: https://leetcode.com/problems/product-of-array-except-self/
'''

class Solution:
	'''
	Each element of our desired output consists of a product of two values: the product of all elements prior to that element,
	and the product of all elements after that element. We can construct two arrays, each requiring one linear iteration: one for the product of all elements prior 
	to element i, and one for the product of all elements after element i, and then our final output is simply the Hadamard product of these two arrays.

	Time Complexity: O(n)
	Space Complexity: O(n)
	'''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
        	return []
    
		left_products = [1] * len(nums)
		for i in range(1, len(nums)):
		    left_products[i] = left_products[i-1] * nums[i-1]

		right_products = [1] * len(nums)
		for i in range(len(nums)-2, -1, -1):
		    right_products[i] = right_products[i+1] * nums[i+1]

		return [left_products[i] * right_products[i] for i in range(len(left_products))]


class Solution:
	'''
	Same method as above, but instead of constructing an additional array for the right product, just carry a single value for the product of
	all elements after element i and multiply our left-product array element at that location by it each iteration rather. Then, we can just 
	return our left_products array without using any additional space.

	Time Complexity: O(n)
	Space Complexity: O(1)
	'''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
	    if not nums:
	        return []
	    
	    left_products = [1] * len(nums)
	    for i in range(1, len(nums)):
	        left_products[i] = left_products[i-1] * nums[i-1]
	    
	    right_products= 1
	    for i in range(len(nums)-2, -1, -1):
	        right_products *= nums[i+1]
	        left_products[i] *= right_products
	    
	    return left_products