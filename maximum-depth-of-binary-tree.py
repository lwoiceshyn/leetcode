'''

https://leetcode.com/problems/maximum-depth-of-binary-tree/

'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	'''
	Simple recursion. If we try calling the function on a None object, 
	e.g., a node that doesn't exist, return 0. Otherwise, return 
	1 plus the maximum of the function called recursively on the left
	and right nodes. If both are zero, we are at a leaf node, and thus
	we just return 1. If neither are zero, we explore both nodes to
	their maximum depths, and if either is zero, we just explore the
	child that exists.

	Time Complexity: O(n), where n is the total number of nodes
	Space Complexity: O(h), where h is the height of the tree, since this is the maximum recursion depth we will reach.
	'''
    def maxDepth(self, root):
    	if not root:
    		return 0
 		else:
 			return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))