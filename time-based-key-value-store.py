'''
https://leetcode.com/problems/time-based-key-value-store/
'''

from collections import defaultdict
class TimeMap:
	'''
	Since the values from set are guaranteed to be in order of increasing timestamp,
	our timestamps will form a sorted sequence for each key. In order to find the value in 
	each of the list items which corresponds to the largest time stamp that is <= the
	input time stamp, use binary search, since the list for each value will be sorted.

	Time Complexity: Set: O(1), Get: O(log(values_at_key))
	Space Complexity: O(keys*avg_values_per_key)
	'''
    def __init__(self):
        self.inputs = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.inputs[key].append((timestamp, value))
    def get(self, key: str, timestamp: int) -> str:  
        if key not in self.inputs:
            return ""
        values = self.inputs[key]
        left, right = 0, len(values)-1
        if values[left][0] > timestamp:
            return ""
        if values[right][0] <= timestamp:
            return values[right][1]
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] < timestamp:
                left = mid +1
            elif values[mid][0] > timestamp:
                right = mid - 1
        return values[right][1]





import heapq
class TimeMap2:
	'''
	I initially missed the note that states that all timestamps for set are strictly
	increasing. This solution is best one for the case in which this assumption is not made.

	Use a heap to store the values at each key, sorted by their negative timestamp(since heapq by default is a min-heap). For new
	values coming in, push them onto the heap, to maintain the heap order property.

	For getting them, simply iterate through until we either find one with a timestamp <= current time stamp,
	or not, in which case we return "".

	Time Complexity: Set: O(log(values_at_key)), Get: O(values_at_key)
	Space Complexity: O(key*avg_values_per_key)
	'''
    def __init__(self):
        self.dict = {}
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = [(-timestamp, value)]
        else:
            heapq.heappush(self.dict[key], (-timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict or not self.dict[key]:
            return ""
        else:
            for neg_time, value in self.dict[key]:
                if -neg_time <= timestamp:
                    return value
            return ""