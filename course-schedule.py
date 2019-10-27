'''
https://leetcode.com/problems/course-schedule/
'''


class Solution:
    '''
    Colors method for checking for a cycle in a graph. For simplicity, use -1, 0, and 1 to represent the colors
    grey, white and black. 0 (white) means the node hasn't been processed yet, -1 (grey) means it's currently undergoing DFS,
    and black (1) means that node has already been fully processed and confirmed that no cycle originates from that node. If we
    reach a node marked as -1, a cycle has been detected, so return False. If we reach one marked as 1, then we've already
    done the work for that node, so return True. Otherwise, set the current node to -1, and then call the function recursively on
    all child vertices of that node. If any reutrn False, return False. If we finish DFS on that node with no Falses returning,
    return True. Use a list of nested lists to represent the graph, where the nested list at index i represents the nodes that
    node i leads to, and use a list of integers to store the numbers for every node. Fill in the graph by  going through each
    prerequsite, and for [0,1] for example, 1 is the prerequisite to 0, so append 0 to index 1 in the graph.

    Time Complexity: O(V+E)
    Space Complexity: O(V+E)
    '''
    def dfs(self, i, visited, graph):
        if visited[i] == -1:
            return False
        if visited[i] == 1:
            return True
        visited[i] = -1
        for vertex in graph[i]:
            if not self.dfs(vertex, visited, graph):
                return False
        visited[i] = 1
        return True
    
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses
        for x, y in prerequisites:
            graph[y].append(x)
        for i in range(numCourses):
            if not self.dfs(i, visited, graph):
                return False
        return True


from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        forward = {i: set() for i in range(numCourses)} #key depends on values
        backward = defaultdict(set) #values depend on key
        for a, b in prerequisites:
            forward[b].add(a)
            backward[a].add(b)
        dq = deque([node for node in forward if not forward[node]])
        while dq:
            node = dq.popleft()
            for neighbor in backward[node]:
                forward[neighbor].remove(node)
                if not forward[neighbor]:
                    dq.append(neighbor)
            forward.pop(node)
        return not forward
