'''
https://leetcode.com/problems/course-schedule/

'''

class Solution:
	'''
	This problem essentially boils down to detecting a cycle in a directed graph. If any vertex has a path that leads back to that
	vertex, we have a cyclic dependency in the graph, and thus cannot take all of the courses. To detect a cycle in a graph in
	linear time, we use the color algorithm, which is a modified depth-first search that keeps track of all previously visited 
	nodes to avoid redundancy. The brute force method would be to traverse all vertices and DFS from each of them to detect a cycle.
	Here, we avoid repeated computation by changing the state of each node as we DFS. 

	Initially, we create two representations of the graph using a list of lists, where foward[index] are the classes that depend on 
	class number index, backward[index] are the dependencies of class index and a list called visited, which is initially set to all zeros (white). 
	For our DFS algorithm, we first check for two conditions. If the state of the node in visited is -1 (grey), this node is currently undergoing DFS,
	and we have found a cycle to this node, so return False. If the state of the node in visited is 1 (black), that means we have already
	performed DFS of that node and all descendents and not found a cycle, so return True. If the node is neither of these two states,
	it is 0 (white), thus start the DFS from this node. Set its value to -1 (grey) indicating it is currently undergoing DFS,
	then recursively call dfs on its neighbors, and if that call returns False, return False. If DFS successfully completes
	with returning all True, then set the value of visited for that node to 1 (black), indicating that node and its descendents
	were fully explored and no cycles found.

	Go through all the courses that have no initial dependencies (empty values in backward), and run DFS from those nodes. If the
	DFS call returns False, return False, as a cycle was detected. Then, go through visited, and make sure all nodes are set to 1,
	i.e., they are reachable with searches starting from the non-dependent nodes. Finally, if those pass, return True.

	Time Complexity: O(V+E)
	Space Complexity: O(V+E)
	'''
    def canFinish(self, numCourses, prerequisites):
        forward = [[] for _ in range(numCourses)]
        backward = [[] for _ in range(numCourses)]
        visited = [0] * numCourses
        for x, y in prerequisites:
            forward[y].append(x)
            backward[x].append(y)
        for i in range(numCourses):
            if not backward[i]:
                if not self.dfs(i, visited, forward):
                    return False
        for status in visited:
            if status != 1:
                return False
        return True
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses
        for x, y in prerequisites:
            graph[y].append(x)
        for i in range(numCourses):
            if not self.dfs(i, visited, graph):
                return False
        return True

from collections import deque, defaultdict
class Solution2:
	'''
	This solution is a more logical solution based on Kahn's algorithm (https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/).
	In general, we can start with the classes that have no prerequisites, see what classes these unlock, then see what classes those unlock, etc.,
	and go through this logic until we've either unlocked all the classes, or we're at a stage where we can't unlock any more classes. If the graph
	has any cycles, then we will reach this stage and can return false.

	We define a forward and backward graph, where forward is a dictionary mapping each node to the nodes it depends on, and backward is a dictionary mapping
	each node to the nodes that depend on it. 
	
	Then, we can use a deque to perform a BFS across our unlocked nodes, where the deque will hold the nodes we have currently unlocked, and each stage of the
	BFS will unlock a further set of nodes, until we've either unlocked all of the nodes, or we're unable to unlock any more. We start by populating the deque
	with the nodes that have no dependencies (forward[node] is None). Then, while the deque is not empty, pop the left item. Then, go through all nodes that
	depend on this node (backward[node]), and remove that required dependency from forward. If there's no more dependencies left for that node in forward,
	then add it to our deque. After we've done this for a node, pop the node from forward to indicate that the node has been unlocked and used to unlock
	its dependent nodes. Finally, just return not forward, which will only be True if forward is empty, meaning we've unlocked all nodes and popped them
	from the dictionary.

	Time Complexity: O(V+E)
	Space Complexity: O(V+E)
	'''
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    	forward = {i: set() for i in range(numCourses)} #key depends on values
    	backward = defaultdict(set) #values depend on key
    	for a, b in prerequisites:
    		forward[b].add(a)
    		backward[a].add(b)
    	queue = deque([node for node in forward if not forward[node]])
    	while queue:
    		node = queue.popleft()
    		for neighbor in backward[node]:
    			forward[neighbor].remove(node)
    			if not forward[neighbor]:
    				queue.append(neighbor)
    		forward.pop(node)
    	return not forward


