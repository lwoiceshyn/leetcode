'''
https://www.lintcode.com/problem/meeting-rooms/description
'''
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    This question is simply asking if there are any overlaps between the intervals. First, sort the meeting times by 
    start time, increasing. Then, interate through the sorted intervals, and if the subsequent interval ever has a left 
    bound that is less than the previous intervals' right bound, then there is a conflict, and the person is not
    able to attend all meeting.

    Time Complexity: O(nlogn)
    Space Complexity: O(1)
    """
    def canAttendMeetings(self, intervals):
        intervals = sorted(intervals, key=lambda x:x.start)
        prev_rbound = float('-inf')
        for interval in intervals:
            if interval.start < prev_rbound:
                return False
            else:
                prev_rbound = interval.end
        return True