'''

https://www.lintcode.com/problem/alien-dictionary/description


'''

from collections import defaultdict
class Solution:
    """
    Every pair of words that we analyze from the first to last word in the input list creates a hierarchical
    connection between two characters. When considering a word and its subsequent word, the first difference in
    a character between those two words creates a hierarchy such that the letter in word i > the letter in word i+1.
    All of these hierarchies form a directed graph, where each vertex in the graph is a letter. If we want to print out
    the hierarchy, we simply need to perform a topological sort of the graph. If there are any cycles in the graph,
    then there is a circular hierarchy, and the graph is invalid. 

    We define the graph as a dictionary mapping each character to a set of characters that the character has hierarchy over.
    We also create a set of all of the characters in all of the words in order to iterate through each node
    during our topological sort. Then, we go through each pair of words, and populate our graph by finding the hierarchy and 
    adding that edge to the graph. Then, we perform the topological sort through the graph, appending each value to our results
    list, or, if finding a cycle, returning an empty string to indicate an invalid input. Finally, reverse the output list,
    since we appended in the reverse hierarchy order, and join the characters together to make a string representing
    the hierarchy.
    
    The set we created of all of the characters is mapped to a list, and sorted in reverse, since in the case of there being 
    multiple valid topological orderings, we want to return the one which is in lexicographical order, as the question 
    requires that.

    In the topsort function, we first check if the node has been visited yet. If so, check if the node has already been visited from that root.
    If so, return True, as this indicates a cycle. If not, add it to visited, indicate the root from which
    the DFS is being called from, and then recursively call topsort on all of its neighbors. If any of those calls return True, then 
    a cycle was found, so just return True all the way up the recursion. Otherwise, once the neighbors have all been processed, or
    we've reached a leaf node, append it to our results. If we've visited all nodes and not found any cycles, return False.

    Time Complexity: O(V + E), 
    Space Complexity: O(V + E)
    where V=c, and E=c^2, c being the number of unique characters in the input
    """
    def alienOrder(self, words):
        hierarchy = defaultdict(set)
        nodes = sorted(list(set(''.join(words))), reverse=True)
        for i in range(1, len(words)):
            min_range = min(len(words[i-1]), len(words[i]))
            for j in range(min_range):
                if words[i-1][j] != words[i][j]:
                    hierarchy[words[i-1][j]].add(words[i][j])
                    break
        res = []
        visited = {}
        for node in nodes:
            if self.topSortDFS(node, node, hierarchy, res, visited):
                return ""
        return "".join(res[::-1])
    
    def topSortDFS(self, root, node, hierarchy, res, visited):
        if node not in visited:
            visited[node] = root
            for neighbor in hierarchy[node]:
                if self.topSortDFS(root, neighbor, hierarchy, res, visited):
                    return True
            res.append(node)
        elif visited[node] == root:
            return True
        return False
            