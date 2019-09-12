'''
https://leetcode.com/problems/insert-interval/
'''


class Solution:
	'''
	If the interval cleanly fits into the list, its left bound will be greater than the right bound
	of the previous interval, and its right bound will be less than the left bound of the next interval.

	To handle the merging, we reconstruct the list by iterating through the original interval list. First,
	check if the right bound of the interval from the list is less than the left bound of the new interval.
	If so, append the old interval to the list. Next, check if the left bound of the old interval is greater
	than the right bound of the new interval. If so, the new interval cleanly fits into the existing list,
	so simply append it, append the rest of the intervals, and return.

	In the third case, the left bound of the new interval is less than the right bound of the old interval,
	or the right bound of the new interval is greater than the left bound of the new interval. In either case,
	we have to merge the two intervals. This is done easily by taking the minimum of their left bounds,
	and the maximum of their right bounds. Update the new interval to this merged interval each time
	we reach this case so that we easily merge multiple old intervals, if necessary.

	Finally, if we exited the loop without returing, append the new interval to the list we made, since in this case
	our new interval belongs at the end.

	Time Complexity: O(n)
	Space Complexity: O(n)
	'''
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res, new = [], newInterval
        for i, old in enumerate(intervals):
            if old[1] < new[0]:
                res.append(old)
            elif new[1] < old[0]:
                res.append(new)
                return res + intervals[i:]
            else:
                new[0] = min(new[0], old[0])
                new[1] = max(new[1], old[1])
        res.append(new)
        return res    

