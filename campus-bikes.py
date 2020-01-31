'''
https://www.leetcode.com/campus-bikes/ (Premium)

Problem Description:

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


Solution:

Go through every worker, and for each worker, check every bike. Create a mapping which stores the L1 distance
to each bike for each worker, in descending order, such that the shortest distance bike can be popped from the
end of the list. Store the mapping as a list of nested tuples, where each tuple follows (distance, worker, bike),
for tuple comparison purposes later.

Then, create a min heap of size(num_workers), which will store the current bicycle which is the shortest distance to
each worker, from shortest to longest. Also create a set to keep track of which bikes have already been assigned to
a worker. Then, check while the size of the set is still less than the number of workers (not every worker has 
been assigned a bike yet), pop the min value from the heap (sorted by distance first, then worker ID, then bike ID
due to the tuple representation). Check if the bike is in the set already. If not, assign the bike to worker, and add
it to the set. If so, get the next best bike in terms of distance for that worker and push it into the heap.

Time Complexity: O(M*N), where M and N are the number of workers and bikes.
Space Complexity: O(M), since all of the data structures used are linear in 
the number of total workers.
'''
class Solution:
   def assignBikes(self, workers, bikes):
        distances = []     
        for i, (x, y) in enumerate(workers):
            distances.append([])
            for j, (x_b, y_b) in enumerate(bikes):
                distance = abs(x - x_b) + abs(y - y_b)
                distances[-1].append((distance, i, j))
            distances[-1].sort(reverse = True) 

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

