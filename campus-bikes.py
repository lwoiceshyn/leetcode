'''
https://www.leetcode.com/campus-bikes/ (Premium)

On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M. Each worker 
and bike is located on a coordinate on this grid.

Our goal is to assign a bike to each other. Among the available bikes and workers, we choose the
(worker, bike) pair with the shortest L1 distance between each other, and assign the bike
to that worker. If there are multiple (worker,bike) pairs with the same shortest L1 distance,
choose the pair with the smallest worker index. If there are multiples here, choose the pair
with the smallest bike index. 

Repeat this process until there are no more available workers.

Return a vector ans of length N, where ans[i] is the index (0-indexed) of the bike 
that the ith worker is assigned to.

Example input:
workers = [[0,0], [2,1]]
bikes = [[1,2], [3,3]]

Output: [1,0]

Note: 1 <= N <= M <= 1000 (There is at least 1 worker, 1 bike, and no more than 1000 of each for any input case)

Thought Process:
Brute Force: Go through every worker, bike pair, compute the distance, and store those values,
-We now have a data structure mapping every pair of worker/bike to a distance value.
-Sort the distance values in increasing order.
-start making assignments by iterating through the distance values, and removing workers 
once an assignment has been made to them. settle disputes as discussed above.
-convert the worker:bike assignments structure to the desired output list

O(m*n)
'''
class Solution:
   def assignBikes(self, workers, bikes):
        distances = []     # distances[worker] is tuple of (distance, worker, bike) for each bike 
        for i, (x, y) in enumerate(workers):
            distances.append([])
            for j, (x_b, y_b) in enumerate(bikes):
                distance = abs(x - x_b) + abs(y - y_b)
                distances[-1].append((distance, i, j))
            distances[-1].sort(reverse = True)  # reverse so we can pop the smallest distance

        result = [None] * len(workers)
        used_bikes = set()
        queue = [distances[i].pop() for i in range(len(workers))]   # smallest distance for each worker
        heapq.heapify(queue)

        while len(used_bikes) < len(workers):
            _, worker, bike = heapq.heappop(queue)
            if bike not in used_bikes:
                result[worker] = bike
                used_bikes.add(bike)
            else:
                heapq.heappush(queue, distances[worker].pop())  # bike used, add next closest bike

        return result

