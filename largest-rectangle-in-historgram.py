'''
https://leetcode.com/problems/largest-rectangle-in-histogram/
'''


class Solution:
	'''
	The most brute force solution would involve going through every contiguous subarray, computing the min height,
	and then computing the area via its length * min height, which would be O(n^3). This solution improves to O(n^2)
	by starting a search from every index moving right, and keeping track of the smallest height encountered so far 
	during that search.

	Time Complexity: O(n^2)
	Space Complexity: O(1)
	'''
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
        	min_height = heights[i]
        	for j in range(i+1, len(heights)):
        		min_height = min(min_height, heights[j])
        		max_area = max(max_area, min_height*(j-i+1))
        return max_area


class Solution2:
	'''
	Note: Asking this question expecting someone to come up with this solution on the fly is ridiculous

	Stack solution:
	If we consider every individual rectangle as a potential starting point, whenever we come across a
	new rectangle which is smaller in height, we know for a fact that the previously larger rectangle
	cannot be a starting point anymore, and thus we can calculate the areas that this rectangle forms
	with all of the previous rectangles for which height > height of the new rectangle. We use a stack
	to store the rectangles we've already seen. When we see a new rectangle with height >= the last
	rectangle in the stack, append it to the stack. When we come across a smaller height rectangle than
	the last rectangle in the stack, start removing rectangles and calculate the area they form from their
	start point to the right bound of the first rectangle we popped, until we reach one with height that
	is <= the small rectangle we came across. In this case, append the current to the stack, and continue
	onwards. 

	Initialize the stack with a -1 value to start with, so that the while loop check will not be invalid 
	for the first value in heights.

	To handle the calculation for the area between the shortest rectangle in the histogram and the width
	it spans, which will be the last remaining value in the stack when we reach the end, append a 0 to 
	the histogram, so that when this last value is reached, it will calculate this final area, in 
	case this is the max area.

	Time Complexity: O(n)
	Space Complexity: O(n)
	'''
    def largestRectangleArea(self, heights: List[int]) -> int:
    	stack = [-1]
    	max_area = 0
    	heights.append(0)

    	for i in range(len(heights)):
    		while heights[i] < heights[stack[-1]]:
    			h = heights[stack.pop()]
    			w = (i-1 - stack[-1])
    			max_area = max(max_area, h*w)
    		stack.append(i)

    	return max_area