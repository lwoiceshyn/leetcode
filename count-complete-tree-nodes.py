'''
https://leetcode.com/problems/count-complete-tree-nodes/
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	'''
	Simple recursive counting. If called on a leaf node, return 1. If called on a non-existent node, return 0.
	Otherwise, add 1 to the sum of the nodes from the left and right subtrees.

	Time Complexity: O(n)
	Space Complexity: O(log(n)), since the tree is complete, and therefore balanced.
	'''
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return 1 + self.countNodes(root.left)+ self.countNodes(root.right)

 class Solution:
 	'''
 	If we check the depth of the left and right subtrees, we can determine which half is a complete binary tree. 
 	If the depth of the left and right subtrees is different, we know that the right subtree has to be a complete binary
 	tree with the bottom level fully filled-in. If they're the same, then we know that at least the left subtree has to 
 	be a complete binary tree with the bottom level fully filled-in. For each of these cases, the number of total nodes
 	in that subtree is 2^(depth). Then, we can call the function recursively on the opposite subtree and keep breaking the 
 	problem down until we hit our base case of an empty subtree, where we return 0.
	
	Time Complexity: O(log(n)^2)
	Space Complexity: O(log(n))
 	'''
    def countNodes(self, root):
        if not root:
            return 0
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        if left_height == right_height:
            return 2 ** left_height + self.countNodes(root.right)
        else:
            return 2 ** right_height + self.countNodes(root.left)

    def get_height(self, root):
        if not root:
            return 0
        return 1 + self.get_height(root.left)