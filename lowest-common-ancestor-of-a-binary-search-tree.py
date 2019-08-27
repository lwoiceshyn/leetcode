'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

'''	

class Solution:
	'''
	There are three cases when considering a BST and two nodes in the BST other than the root:
	If p is in the left subtree, and q is in the right subtree, then the root is simply the 
	LCA. This includes the case where either p or q is the root node as well. In the other two cases 
	(both p and q are either in the left and right subtree), we need to walk down that tree's leftmost 
	or rightmost branch until either p or q are the current node, or p and q are in separate subtrees of that node.

	Time Complexity: O(h), which is O(logn) if balanced.
	Space Complexity: O(h)
	'''
	def lowestCommonAncestor(self, root, p, q):
		if not (p or q or root)
			return None
		if p.val < root.val and q.val < root.val:
			return self.lowestCommonAncestor(root.left,p,q)
		elif p.val > root.val and q.val > root.val:
			return self.lowestCommonAncestor(root.right,p,q)
		else:
			return root

class Solution2:
	'''
	Iterative version of the above code. Every iteration, check if both p and q values
	are either in left or right subtree. If not, then they must be either in separate 
	subtrees of the current node, or one of the two is the node, in which case 
	the current node is the LCA.

	Time Complexity: O(h)
	Space Complexity: O(1)
	'''
	def lowestCommonAncestor(self, root, p, q):
		while root:
			if p.val > root.val and q.val > root.val:
				root = root.right
			elif p.val < root.val and q.val < root.val:
				root = root.left
			else:
				return root
