'''
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
'''
class Solution:
    '''
    Simple recursive inorder traversal where we recursively pass a list through
    as we perform the traversal, and append values to it in order. Then we know
    that the k-1 index value from the inorder traversal list is the kth smallest
    value.

    Time Complexity: O(n)
    Space Complexity: O(n)
    '''
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return self.inorder(root, [])[k-1]
    def inorder(self, root, vals):
        if not root:
            return
        self.inorder(root.left, vals)
        vals.append(root.val)
        self.inorder(root.right, vals)
        return vals



class Solution2:
    '''
    Similar solution as above, but uses a class variable to track how far into
    the traversal we are. Every time we reach the root portion of the inorder traversal,
    we subtract one from our class variable k, and once that is 0, aka, we're at the kth
    node in the inorder traversal, we know we are at the kth smallest node, so save this
    result to a class variable. Also check if the class variable k is ever less than 0,
    and if so, don't bother with that function call since we've already hit the kth
    node earlier.

    Time Complexity: O(n)
    Space Complexity: O(h)
    '''
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.res = None
        self.inorder(root)
        return self.res
    def inorder(self, root):
        if not root or self.k < 0:
            return
        self.inorder(root.left)
        self.k -= 1
        if self.k == 0:
            self.res = root.val
            return
        self.inorder(root.right)

class Solution3:
    '''
    In order to solve this iteratively, we need to mimic an inorder traversal of the tree. To do this,
    we use a stack, in which we use to represent all the left-most nodes in the current branch we are in.
    We go down as far left as possible until there are no more left children, then pop the last node off the stack,
    and reduce k by 1. Then, we check if we've hit the kth node in the traversal yet (k == 0), and if not, we assign
    root to root.right, and then try and go as far down that branch's left nodes and repeat the process until we've
    found the value we're looking for.

    Time Complexity: O(n)
    Space Complexity: O(h)
    '''
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
              return root.val
            elif k < 0:
              return
            else:
              root = root.right