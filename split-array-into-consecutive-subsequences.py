'''
https://leetcode.com/problems/split-array-into-consecutive-subsequences/
'''


import heapq
class Solution:
	'''
	Use a dictionary that contains a mapping from the last integer value in a current subsequences to a priority queue of lengths of all
	subsequences we've currently built that end in that value. Iterate through each number. 

	Check if a subsequence one less than the current number exists by checking if one less than the current number is a key in the dictionary. 
	If not, check if the current number is already a key in the dictionary. If not, create a new priority queue with only the element 1 in it, 
	indicating a priority queue with one sequence of length 1. If already exists, then add a 1 to the existing priority queue.

	If a number one less than than the current does exist, then pop the sequence with the shortest length from that priority queue, and add 1
	to its length. If the prirority queue is now empty, then delete it from the dictionary. If the current number (which now ends the current sequence)
	isn't a key, create a new priority queue with the new length as its only value. Otherwise, push to the existing priority queue.
	
	Finally, iterate through all the priority queues and check if any have a minimum value of less than 3. If so, return False, if not, return True.

	Time Complexity: O(N * log(s)), where N is the input length, and maximum priority queue size, which is is the max number of total different sequences 
	ending in the same value that will exist for some input.

	Space Complexity: O(N), since worst case scenario every number is disjoint and forms its own unique key in the hashtable.
	'''
    def isPossible(self, nums: List[int]) -> bool:
        sequences = {}
        for num in nums:
            if num-1 not in sequences:
                if num not in sequences:
                    sequences[num] = [1]
                else:
                    heapq.heappush(sequences[num], 1)
            else:
                length = heapq.heappop(sequences[num-1]) + 1
                if len(sequences[num-1]) == 0:
                    del sequences[num-1]
                if num not in sequences:
                    sequences[num] = [length]
                else:
                    heapq.heappush(sequences[num], length)
        for lengths in sequences.values():
            if min(lengths) < 3:
                return False
        return True