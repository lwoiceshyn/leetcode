'''

https://www.lintcode.com/problem/graph-valid-tree/description

'''

from collections import defaultdict
class Solution:
    '''
	In order for an undirected graph to represent a valid tree, there are two conditions that have to be met. Firstly, If we search the graph
	from any given vertex, we should be able to reach all other vertices in the graph, i.e., the graph should be connected. Secondly, the graph
	should contain cycles. If we start a search from any random vertex, we should never reach a vertex that we have already visited.

	In order to do this properly, we use a depth-first search function that is designed to start from any random vertex, and perform a DFS 
	from that vertex, adding any new vertex we find to a set of a visited vertices. We also keep track of the last node we visited and prevent
	traveling back to that node immediately after, since we're dealing with an undirected graph, and want to restrict being able to immediately
	backtrack to the previous node. If at any point in this DFS, we reach a node that we've already visited previously, then we know that there
	is a cycle, and can return False. If we finish the DFS and haven't visited all nodes, then this is an invalid tree, so return False. Otherwise,
	return True.

	I use a dictionary of int:set(int) key:value mappings, where the sets are the nodes connected to that vertex. Then, simply call the DFS function
	from the first node, which will return True if it hits a cycle. If that happens, return False, or if we didn't visit all nodes, return False.

	Time Complexity: O(V)
	Space Complexity: O(V)
    '''
    def validTree(self, n, edges):
        if not edges:
            if n == 1:
                return True
            else:
                return False
        graph = defaultdict(set)
        for x, y in edges:
        	graph[x].add(y)
        	graph[y].add(x)
    
        if len(graph) != n:
        	return False
        visited = set()
        if self.undirectedDFS(0, None, graph, visited):
        	return False
        if len(visited) != n:
        	return False
        return True
        
    def undirectedDFS(self, node, prev, graph, visited):
        if node not in visited:
            visited.add(node)
            neighbors = graph[node]
            for neighbor in neighbors:
                if neighbor != prev:
                    if self.undirectedDFS(neighbor, node, graph, visited):
                        return True
            return False
        else:
            return True

