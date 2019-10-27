'''

https://leetcode.com/problems/clone-graph/


Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

 

Example:
1 - 2
|   |
3 - 4


Input:
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

Explanation:
Node 1's value is 1, and it has two neighbors: Node 2 and 4.
Node 2's value is 2, and it has two neighbors: Node 1 and 3.
Node 3's value is 3, and it has two neighbors: Node 2 and 4.

'''

class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution:
	'''
	Recursive depth-first search solution. Use a dictionary to track if a node has been visited yet or not. If it hasn't, then create a new node
	with that node's value, and create a mapping between the original and copy node in the dictionary. Then, iterate through the 
	neighbors of the original node. If they have been visited before, and thus a copy already made, simply append the copy of the neighbor to
	the copied nodes' neighbors list by fetching it with the dictionary. Otherwise, call the function recursively on that neighbor and append the
	returned node from the recursive call to neighbors.

	Time Complexity: O(n) - All vertices visited once
	Space Complexity: O(n) - Recursion trace in worst case scenario of nodes being a linked list.
	'''
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}
        def dfs(node):
        	if node in visited:
        		return
            node_copy = Node(node.val, [])
            visited[node] = node_copy
            for neighbor in node.neighbors:
                if neighbor in visited:
                    node_copy.neighbors.append(visited[neighbor])
                else:
                    node_copy.neighbors.append(dfs(neighbor))
            return node_copy
        return dfs(node)

from collections import deque
class Solution2:
	'''
	Iterative breadth-first-search solution. Also uses a dictionary to track nodes that have been visited so far. Start with creating
	a copy of the initial node, adding the copy to the dictionary, and adding that node to a deque that will store all nodes we are
	iterating through. Then, use a while loop to perform the BFS. Take the current node, and go through its neighbors. If the 
	neighbor exists in the dictionary, then simply append it to the copied version of the current nodes neighbor list. If it
	doesn't exist yet, create the copy, add it to the dictionary, add it to the neighbors list of the current node, and then
	add it to the deque.

	Time Complexity: O(n) - All vertices visited once
	Space Complexity: O(1) - Other than the copied graph, no additional space complexity used.
	'''
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        visited = {}
        copy_node = Node(node.val, [])
        visited[node] = copy_node
        queue = deque([node])
        while queue:
            curr_node = queue.popleft()
            for neighbor in curr_node.neighbors:
                if neighbor in visited:
                    visited[curr_node].neighbors.append(visited[neighbor])
                else:
                    neighbor_copy = Node(neighbor.val, [])
                    visited[neighbor] = neighbor_copy
                    visited[curr_node].neighbors.append(neighbor_copy)
                    queue.append(neighbor)
        return visited[node]
      