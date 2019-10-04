'''
https://leetcode.com/problems/find-median-from-data-stream/
'''
import heapq
class MedianFinder:
	'''
	For the median of an array of a sorted array of numbers, we simply need to check if it's even or odd
	length, and then return either then center value, or the mean of the two center values. However, sorting
	an array is O(nlogn), and is inefficient in the sense we don't actually care about the rest of the sorted numbers 
	being sorted. 

	Instead, we can use two heaps to each store half of our numbers, such that one heap is a max heap storing the bottom
	half of all numbers by value, and one heap is a min heap storing the top half of all numbers by value. Then, we can
	get the two center numbers by simply peeking at the min and max values of these heaps. If the low heap is one value
	shorter than the max heap, simply return the min of the high heap. Otherwise, return the average of the max value
	in the low heap and the min value in the high heap.

	The heapq module is only a min heap, so we need to reverse the polarity of all numbers in the low heap such that it
	is effectively a max heap, storing a min heap of the negative of all numbers in the heap, and when we want the max
	value from it, simply, extract the minimum and reverse its polarity.

	When adding a new number, instead of deliberately checking what heap to put the number into, we use the following
	convention: 

	The upper heap will always contain either n/2 or n/2 +1 values. If the two heaps are the same length,
	then we are increasing the length of the upper heap by 1. Instead of checking where the number belongs deliberately,
	simply first push it into the low heap, pop out the max value from the low heap, then push this max value to the
	upper heap.

	If the upper heap is 1 longer, then we are adding a value to the lower heap. Again, instead of deliberately checking
	where the number belongs based on magnitude, push it into the upper heap, pop the min value from the upper heap, and
	then push this value to the lower heap.
	'''
    def __init__(self):
        self.low_heap = []
        self.high_heap = []

    def addNum(self, num: int) -> None:
    	'''
    	Time Complexity: O(logn), as all heap insertion and root extraction methods are.
    	'''
        if len(self.low_heap) == len(self.high_heap):
            heapq.heappush(self.high_heap, -heapq.heappushpop(self.low_heap, -num))
        else:
            heapq.heappush(self.low_heap, -heapq.heappushpop(self.high_heap, num))

    def findMedian(self) -> float:
    	'''
    	Time Complexity: O(1).
    	'''
        if len(self.low_heap) == len(self.high_heap):
            return (self.high_heap[0] - self.low_heap[0]) / 2
        else:
            return self.high_heap[0]
