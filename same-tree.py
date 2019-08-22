'''
https://leetcode.com/problems/same-tree/

'''

class Solution:
	'''
	In order to check if these are the same, perform a simultaneous preorder traversal (root, left, right), ensuring 
	each tree has the same values at every corresponding node. First check if both nodes exist. If so, check that
	their root values match, then call the function recursively on their left node and right node. Finally,
	if either or both nodes don't exist, return p == q, which will return True in the case that both nodes being
	checked are None, and False otherwise.

	Time Complexity: O(n)
	Space Complexity: O(h), where h is the height of the shorter of the two trees.
	'''
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    	if p and q:
        	return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p == q

class Solution2:
	'''
	Same as above but simply appends nodes in preoder traversal order to a list, including None appended
	wherever a left or right child node doesn't exist. Then simply does a comparison by the traversal lists
	returned from each of the two traversals. Less elegant than the other solution but for some reason runs
	much faster on Leetcode.

	Time Complexity: O(n)
	Space Complexity: O(n+h), where h is the height of the taller of the two trees.
	'''
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.preorder(p) == self.preorder(q)
    def preorder(self, root):
        if not root:
            return [None]
        nodes = [root.val]
        if root.left:
            nodes += self.preorder(root.left)
        else:
            nodes += [None]
        if root.right:
            nodes += self.preorder(root.right)
        else:
            nodes += [None]
        return nodes

class Solution3:
	'''
	Depth-first search using a stack. First, add the root nodes to the stack. Then, start a while loop. Pop the last item off the stack, and check
	if both nodes are not None, in which case both trees match, so continue to the next iteration. If that's not the case, check if only one of the
	nodes is None, and return False if so. Lastly, check if both values are not the same. If so, return False. Otherwise, append the left node pairs
	then right node pairs to the stack. 
	
	Time Complexity: O(n)
	Space Complexity: O(h), where h is the height of the shorter of the two trees.
	'''
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack = [(p, q)]
        while stack:
        	node1, node2 = stack.pop()
        	if not node1 and not node2:
        		continue
        	if not node1 or not node2:
        		return False
        	if node1.val != node2.val:
        		return False
        	else:
        		stack.append((node1.right, node2.right)) 
        		stack.append((node1.left, node2.left))
        return True
