'''

https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph

'''
from collections import defaultdict
class Solution:
   	'''
	Use a set to track the nodes we haven't visited yet. While there's nodes left in that set, do a DFS on a random node
	from that set and mark all nodes visited during that DFS, and increase the component counter by 1. Keep doing this 
	until all nodes have been visited, and then return the count variable which is tracking the number of components.

	Time Complexity: O(V+E)
	Space Complexity: O(V)
    '''
	def countComponents(self, n, edges):
	    graph = defaultdict(set)
	    for x, y in edges:
	    	graph[x].add(y)
	    	graph[y].add(x)

	    remaining_nodes = set(i for i in range(n))
	    count = 0
	    
	    visited = set()
	    while remaining_nodes:
	    	count += 1
	    	self.undirectedDFS(remaining_nodes[0], None, visited)
	    	for node in visited:
	    		remaining_nodes.remove(node)
	    		visited.remove(node)
	    return count

	def undirectedDFS(self, node, prev, visited):
		if node not in visited:
			visited.add(node)
			neighbors = graph[node]
			for neighbor in neighbors:
				if neighbor != prev:
					self.undirectedDFS(neighbor, node, visited)



class Solution2:
    def countComponents(self, n, edges):
	   	'''
		Same method as above but more minimalistic in code. Simply use a list with each element 
		being 0 (unvisited) or 1 (visited). Then simply iterate through this list, and if the
		element has been visited, move to the next one, and if note, perform a DFS from this
		element and mark all vertices in that DFS as visited, and increment the component count by 1.

		Time Complexity: O(V+E)
		Space Complexity: O(V)
    '''
        def dfs(node):
        	if visited[node] == 1:
        		return 
        	else:
        		visited[node] = 1
        		for node1, node2 in edges:
        			if node1 == node:
        				dfs(node2)
        			elif node2 == node:
        				dfs(node1)

        res = 0
        visited = [ 0 for i in range(n)]
        for i in range(n):
        	if visited[i] == 0:
        		dfs(i)
        		res += 1
        return res