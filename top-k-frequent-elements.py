'''
https://leetcode.com/problems/top-k-frequent-elements/
'''
from collections import defaultdict
import heapq
class Solution:
	'''
	First, use a dictionary to store the counts of each number in nums, which takes linear time.
	Then, build a heap out of the dictionary pairs, with the frequency of the number as its key
	in the heap, and the number itself as the value. Since heapq uses a min heap by default, we
	can reverse the polarity of the frequencies to find the k lowest negative frequencies instead.

	Add each dictionary item to the heap and then call heapify on it, which is also linear time. Then simply
	extract the min off the heap k times, and append the corresponding number which that negative frequency
	corresponds with to our output list.

	Note: Building a heap from an unsorted list of keys takes linear time if done properly. Running heapify on one 
	node is a function of the height of the tree from which it was called. If we start at the end of our unsorted array,
	and work from end to start, using heapify down on each element, we achieve linear time. This is because the most
	nodes exist at the lowest level of the tree, If we are heapifying down starting at the bottom and moving up,
	the maximum amount of swaps we will need be much smaller than log(n) for the majority of the nodes, and only
	approach log(n) when we get to the start of the tree, where there are hardly any nodes. The total summation
	can be proven to converge to n mathematically using a Taylor series.

	Time Complexity: O(n)
	Space Complexity: O(n)
	'''
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1
        pq = []
        for num, freq in freqs.items():
            pq.append((-freq, num))
        heapq.heapify(pq)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(pq)[1])
        return res