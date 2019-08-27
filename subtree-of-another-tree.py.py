'''

https://leetcode.com/problems/subtree-of-another-tree/

'''

class Solution:
    '''
    Perform a preorder traversal of s, and at every node t, perform a check if that node is equal to t,
    using a separate function isSame. First check if we're calling the function on a null pointer, and if
    so, return False. Then, traverse s, and at every node, check the subtree originating from that node is
    identical to t, and if so, return true.
    '''
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        same = self.isSame(s, t)
        if same:
            return True
        left = self.isSubtree(s.left, t)
        right = self.isSubtree(s.right, t)
        return left or right

    def isSame(self, s, t):
        if s and t:
            if s.val == t.val:
                left = self.isSame(s.left, t.left)
                right = self.isSame(s.right, t.right)
                if left and right:
                    return True
            else:
                return False
        return s == t


class Solution2:
    '''
    Same solution as above, but written more concisely with all of the recursive checks performed on one line.
    '''
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        return self.isSame(s,t) or (self.isSubtree(s.left,t) or self.isSubtree(s.right,t))

    def isSame(self, s, t):
        if s and t:
                return s.val == t.val and self.isSame(s.left, t.left) and self.isSame(s.right, t.right)
        return s == t

