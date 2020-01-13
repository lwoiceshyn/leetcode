'''
https://leetcode.com/problems/binary-tree-maximum-path-sum/
'''


class Solution:
	'''
	At any node in the tree, the max path sum containing that node is either that node alone,
	that node plus the max path sum containing that node plus the max path sum containing its
	left node, the max path sum containing that node plus the max path sum containing its right node,
	or the max path sum of that node plus the max path sums of both of its children. If we find the
	max path sum at every node, then we will have found the global max path sum in the tree.

	The tricky part is that when we consider the max path sums of the two children, we cannot form a path
	from the parent to the max path sums of a child node that include both of its child nodes, since that
	path is not valid. Thus, we need a way to store the max path sums that include a node and its two children,
	but not pass this max path sum upwards as it cannot be considered in the max path sum of its parent node.

	Thus, we use a class variable to store the maximum globally, and update this max at every node with the
	max path sum of that node including both its children, but only pass the max path sum of that node plus
	either of its children, or that node itself, up to its parent.

	Time Complexity: O(n)
	Space Complexity: O(h)
	'''
    def maxPathSum(self, root):
        self.res = float('-inf')
        self.maxToNode(root)
        return self.res

    def maxToNode(self, node):
        if not node:
            return 0
        left_max = self.maxToNode(node.left)
        right_max = self.maxToNode(node.right)
        full = node.val + left_max + right_max
        either = node.val + max(left_max, right_max, 0)
        self.res = max(self.res, full, either)
        return either

class Solution2:
	'''
	Same solution as above but doesn't rely on class variables, and instead returns a list where the
	first value in the list is the max path sum that we can add to the parent potentially to extend
	the path, and the second is the global maximum that we've found so far, including all local
	paths which horseshoe around the node and its two children.

    Time Complexity: O(n)
    Space Complexity: O(h)
	'''
    def maxPathSum(self, root):
        def max_to_node(node):
            if not node:
                return [float('-inf')] * 2
            left = max_to_node(node.left)
            right = max_to_node(node.right)
            either = node.val + max(left[0], right[0], 0)
            full = node.val + left[0] + right[0]
            global_max = max(full, either, left[1], right[1])
            return [either, global_max]
        return max_to_node(root)[1]


