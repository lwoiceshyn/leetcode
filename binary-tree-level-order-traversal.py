'''
https://leetcode.com/problems/binary-tree-level-order-traversal/

'''


class Solution:
	'''
	Simple iterative depth-first search solution. Use a list to store all the nodes at a certain level of the tree, starting with the root node.
	Then, every iteration, check if there are nodes left in the levels list, and append a list of all the values in the level list to the 
	return list. Then, add all leaf nodes of the nodes in the level list, from left to right, to a temporary list, and then assign the level
	list to the temporary list.

	Time Complexity: O(n)
	Space Complexity: O(n)
	'''
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        level = [root]
        ret = []
        while level:
            ret.append([node.val for node in level])
            temp = []
            for node in level:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            level = temp
        return ret
	

class Solution2:
	'''
	Same method as above but more compact using a single list comprehension to reassign level without
	needing an explicit temp list.

	Time Complexity: O(n)
	Space Complexity: O(n)
	'''
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ret, level = [], [root]
        while root and level:
            ret.append([node.val for node in level])
            level = [child for node in level for child in (node.left, node.right) if child]
        return ret
	
class Solution3:
	'''
	Depth-first, recursive, preorder traversal solution. Track what level we are in at each recursive call, and pass our
	answer list in each recursive call. If a nested list already exists for that level, then extend it with the value that we've
	found, and it not, append a new list to the answer list. Since we're doing DFS from left to right, each nested list will,
	at the end of the search, store all of the node values from left to right as well.

	Time Complexity: O(n)
	Space Complexity: O(n)
	'''
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
        	return []
        else:
        	return self.traverse(root, 1, [])

    def self.traverse(self, node, level, ans):
    	if not node:
    		return

    	if level > len(ans):
    		ans.append([node.val])
    	else:
    		ans[level-1].extend([node.val])
    	self.traverse(node.left, level+1, ans)
    	self.traverse(node.right, level+1, ans)