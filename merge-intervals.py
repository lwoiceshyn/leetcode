'''

https://leetcode.com/problems/merge-intervals/

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

'''

class Solution:
	'''
	First, sort the intervals by left bound. Then, create an empty list which will be used to
	merge the intervals when necessary. Iterate through the intervals in order of increasing
	left bound. If the results list is empty, e.g., we are looking at the first interval, simply
	append it. Otherwise, check if the next interval overlaps with the last interval in the
	results list. This is done by comparing the right bound of the last interval in results
	and the left bound of the current interval we are iterating on. If the left bound of this
	interval is less than or equal to the right bound of the last interval in results, then these
	two intervals overlap. In this case, modify the last interval in results to a merged version of
	the two, by setting the the right bound to the 	maximum of their right bounds. We don't have to
	modify the left bound since we sorted by increasing left bound, meaning the interval in results
	will already have a left bound less than or equal to the interval we are evaluating.

	Time Complexity: O(nlogn)
	Space Complexity: O(n)
	'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x:x[0])
        res = []
        for i, interval in enumerate(intervals):
        	if res and res[-1][1] >= interval[0]:
        		res[-1][1] = max(res[-1][1], interval[1])
        	else:
        		res.append(interval)
        return res
