'''
https://www.lintcode.com/problem/meeting-rooms-ii/description

'''
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    Naive solution. Sort the intervals by increasing left bound, and create an empty list which will contain nested
    lists representing rooms. If no rooms exist, append the current interval, wrapped in a list, to the rooms list. Otherwise,
    find the first room which doesn't conflict with the interval, and append it. If no rooms that don't conflict exist, create
    a new room by appending it to rooms, wrapped in a list. Then, simply return the length of the rooms list as the number
    of required rooms.

    Time Complexity: O(nm), where n is # of intervals, m is # of rooms required. Sorting the intervals is O(nlogn), then iterating through 
                     the intervals and for each interval, iterating through the rooms, is O(mn)
    
    Space Complexity: O(n) - Space needed for the rooms lsit.
    """
    def minMeetingRooms(self, intervals):
        rooms = []
        intervals = sorted(intervals, key=lambda x:x.start)
        for interval in intervals:
            if rooms:
                for room in rooms:
                    if room[-1].end <= interval.start:
                        room.append(interval)
                        break
                else:
                    rooms.append([interval])
            else:
                rooms.append([interval])
        return len(rooms)

import heapq
class Solution2:
    """
    Similar to the above solution but more efficient. Instead of looking at all of the current meeting rooms being used to see
    where the next meeting can slot in, we can simply only check the meeting room with the earliest ending meeting. We use a 
    priorityqueue to store the meeting end times in. If a meeting doesn't overlap with the earliest ending meeting, update that
    rooms end time in the priority queue. Otherwise, add the current meetings end time to the priority queue. Finally, return
    the length of the priority queue.

    Time Complexity: O(nlogn) - Sorting the intervals is O(nlogn), and heap operations(insert, extract_min, heapify) are logn, so 
                                iterating through the intervals and doing heap operations is also O(nlogn)
    Space Complexity: O(n) - Space needed for the heap.
    """

    def minMeetingRooms(self, intervals):
        intervals = sorted(intervals, key=lambda x:x.start)
        pq = [intervals[0].end]
        heapq.heapify(pq)
        for interval in intervals[1:]:
            if heapq.nsmallest(1,pq)[0] <= interval.start:
                heapq.heappushpop(pq,interval.end)
            else:
                heapq.heappush(pq,interval.end)
        return len(pq)
