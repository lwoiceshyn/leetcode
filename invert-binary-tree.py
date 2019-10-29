'''

https://leetcode.com/problems/invert-binary-tree/

'''

class Solution:
	'''
	Depth-first search solution using a stack. Take the current node off the stack, reverse its children,
	if they exist, then add its children to the stack.
	
	Time Complexity: O(n)
	Space Complexity: O(h)
	'''
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return root

class Solution2:
	'''
	Recursive preorder traversal, first reverse the two children, if both or one exists,
	then call the function recursively on the children. Once all recursive calls are finished
	and base cases have been hit (called on None or on leaf node), original function call
	will return the root of the tree.

	Time Complexity: O(n)
	Space Complexity: O(h)
	'''
    def invertTree(self, root: TreeNode) -> TreeNode:
    	if not root:
    		return None
    	if root.left and root.right:
    		root.left, root.right = root.right, root.left
    	elif root.left:
    		root.right = root.left
    		root.left = None
    	elif root.right:
    		root.left = root.right
    		root.right = None
    	else:
    		return root
    	self.invertTree(root.left)
    	self.invertTree(root.right)
    	return root

class Solution3:
	'''
	Elegant recursive solution.

	Time Complexity: O(n)
	Space Complexity: O(h)	
	'''
	def invertTree(self, root: TreeNode) -> TreeNode:
    if root:
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


