'''
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

'''
class Solution:
	'''
	The preorder traversal list starts with the root of the tree, then the next elements
	represent the left tree, and then the right tree. However, just based on this list, we
	don't know how many elements are in which tree. The inorder traversal contains the left 
	tree, then the root, and then the right tree.

	First, take the root node from the preorder traversal list, find its position in the
	inorder traversal list. The number of elements to the left and right represent the 
	number of elements in the left and right subtrees. We can use a simple recursive function
	to find the root, and then assign the left and right children to recursive calls with
	the left and right subtree preorder and inorder traversal lists until we hit the base
	case, where either list is empty.

	Time Complexity: O(n)
	Space Complexity: O(h)
	'''
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        root_index = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:root_index+1], inorder[0:root_index])
        root.right = self.buildTree(preorder[root_index+1:], inorder[root_index+1:])
        return root