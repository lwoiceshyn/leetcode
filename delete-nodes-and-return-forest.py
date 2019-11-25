'''
https://leetcode.com/problems/delete-nodes-and-return-forest/
'''

class Solution:
    '''
    If a node in the tree has a deleted parent, and that node itself isn't deleted, then that node becomes a new root
    in the forest. Recursively walk down the tree with two goals to accomplish: add new roots to the forest, and correctly remove
    them from the tree. The recursive function has a base case of being called on a non-existent child (None), and has an
    argument has_parent, indicating if that recursive call is made from an existing node or a removed node. 

    First, check if the current node is to be deleted. If not, check if it has a parent. If it doesn't, append it to our new forest list. 
    Then, call the function recursively on the left/right children with has_parent set to True, and assign its left/right children to the 
    return of the recursive function call, and finally return the current node, since its not being deleted.

    If the node is to be deleted, then call the function recursively on its children with has_parent set to False, and then return None, since
    the former parent node needs this child set to None, since its being deleted.
    
    Finally, return the list with the forest contained in it.

    Time Complexity: O(n)
    Space Complexity: O(h)
    '''
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        result = []
        def recurse(root, has_parent=False):
            if not root:
                return None
            if root.val not in to_delete:
                if has_parent == False:
                    result.append(root)
                root.left = recurse(root.left, has_parent=True)
                root.right = recurse(root.right, has_parent=True)
                return root
            else:
                root.left = recurse(root.left, has_parent=False)
                root.right = recurse(root.right, has_parent=False)
                return None
        recurse(root)
        return result