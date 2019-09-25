'''
https://leetcode.com/problems/non-overlapping-intervals/
'''

class Solution:
	'''
	First, sort the intervals by left bound, in increasing order. Then, create an empty list and iterate through them. If the interval
	doesn't overlap with the previous one, add it to the list. Otherwise, check which of the two intervals has a smaller right bound,
	meaning it is going to collide with fewer future intervals. Then, return the difference in length between the original list,
	and our new list which doesn't contain any overlapping intervals.

	Time Complexity: O(nlogn)
	Space Complexity: O(n)
	'''
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x:x[0])
        res = []
        for interval in intervals:
            if res and res[-1][1] > interval[0]:
                lower_rbound = min(res[-1], interval, key=lambda x:x[1])
                res[-1] = lower_rbound
            else:
                res.append(interval)
        return len(intervals) - len(res)


class Solution2:
	'''
	Same solution as above, but we don't need to actually use any additional space. Simply keep
	track of the previous right bound, and then whenever we have an overlap, increase the count
	of the removed intervals, and update the previous right bound to the minimum between the
	two overlapping intervals, since that is the interval we keep.

	Time Complexity: O(nlogn)
	Space Complexity: O(1)
	'''
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x:x[0])
        last_rbound = float('-inf')
        removed = 0
        for interval in intervals:
            if interval[0] < last_rbound:
                removed +=1
                last_rbound = min(last_rbound, interval[1])
            else:
                last_rbound = interval[1]
        return removed

