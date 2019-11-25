'''

https://leetcode.com/problems/campus-bikes/

Problem Description:
On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M. Each worker and bike is a 2D coordinate on this grid.
Our goal is to assign a bike to each worker. Among the available bikes and workers, we choose the (worker, bike) pair with the shortest 
Manhattan distance between each other, and assign the bike to that worker. (If there are multiple (worker, bike) pairs with the same shortest 
Manhattan distance, we choose the pair with the smallest worker index; if there are multiple ways to do that, we choose the pair with the smallest bike index).

We repeat this process until there are no available workers. The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|. 
Return a vector ans of length N, where ans[i] is the index (0-indexed) of the bike that the i-th worker is assigned to.

Input: 
workers = [[0,0],[2,1]], 
bikes = [[1,2],[3,3]]
Output: 
[1,0]
'''

import heapq
from collections import defaultdict
class Solution(object):
    def assignBikes(self, workers, bikes):
        """
		
        """
        n, m = len(workers), len(bikes)
        distances = {}
        for i in range(n):
        	distances[i] = []
        	for j in range(m):
        		m_distance = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
        		distances[i].append((m_distance, i, j))
        	distances[i].sort(reverse=True)

        minheap = []
        for i in range(n):
        	minheap.append(distances[i].pop())
        heapq.heapify(minheap)

        res = [None] * len(n)
      	used_bikes = set()

      	while len(used_bikes) < len(workers):
      		_, worker, bike = heapq.heappop(minheap)
      		if bike not in used_bikes:
      			res[worker] = bike
      			used_bikes.add(bike)
      		else:
      			heapq.heappush(minheap, distances[worker].pop())

      	return res


