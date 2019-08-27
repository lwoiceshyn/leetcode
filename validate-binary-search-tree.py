'''

https://leetcode.com/problems/validate-binary-search-tree/

'''

class Solution:
	'''
	Recursive solution that simply does an inorder traversal of the binary tree, using a list
	to track all of the values in the inorder traversal. Then, simply go through all of the values
	in the list from start to end, and if any are not less than the proceding value, then return
	False. Otherwise, return True.

	Time Complexity:O(n)
	Space Complexity: O(n)
	'''
    def isValidBST(self, root):
        inorder =  self.helper(root, [])
        print(inorder)
        for i in range(len(inorder)-1):
            if inorder[i] >= inorder[i+1]:
                return False
        return True

    def helper(self, root, vals):
        if not root:
            return vals
        vals = self.helper(root.left, vals)
        vals.append(root.val)
        vals = self.helper(root.right,vals)
        return vals

class Solution2:
	'''
	Recursive solution that does a preorder traversal, while
	using limits that the value at the current root not breach. Specifically, the 
	upper limit is the value the child node most be smaller than, and the lower limit
	is the value the child node must be larger than. Every time we call the function 
	recursively, we have to update the value that the left child must be less than, aka the
	upper limit, to the parents value, and every time we call the function on a right child , we
	have to update the value that the right child must be greater than, aka the lower limit,
	 to the parents value.

	Thus, we use lower and upper limit parameters as arguments in the recursive function.
	The base case is calling the function on an empty child, in which case just return True.
	Otherwise, ensure that the node value is greater than the lower limit and less than
	the upper limit, then call the function recursively on the left child with an updated upper limit, 
	which is just the current nodes value, and  onthe right child with an updated lower limit, which
	is the nodes current value. If all branches return True, then the BST is valid.

	Time Complexity:O(n)
	Space Complexity: O(h)
	'''
    def isValidBST(self, root, upper_limit=float('inf'), lower_limit=float('-inf')):
    	if not root:
    		return True
    	if root.val >= upper_limit or root.val <= lower_limit:
    		return False

    	return self.isValidBST(root.left, root.val, high) and self.isvalidBST(root.right, low, root.val)