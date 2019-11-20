'''

https://leetcode.com/problems/subtree-of-another-tree/

'''

class Solution:
    '''
    Perform a preorder traversal of s, and at every node t, perform a check if that node is equal to t,
    using a separate function isSame. First check if we're calling the function on a null pointer, and if
    so, return False. Then, traverse s, and at every node, check the subtree originating from that node is
    identical to t, and if so, return true.


    Time Complexity:O(s*t) , at every node in s, we are potentially traversing t nodes to check for sameness, in the worse-case scenario.
    Space Complexity: O(h_s), worst case is s and t being the same tree in which case our recursion trace will go to the height of s.
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
        return self.isSameTree(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)

    def isSameTree(self, s, t):
        if s and t:
                return s.val == t.val and self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
        return s == t

class Solution3:
    '''
    Merkle hash solution (credit to awice on Leetcode discussions). Use a recursive function to go through each tree and create
    a node.merkle object, a hash representing the subtree, involving the merkle hash in inorder order. Then, we can tell that
    the trees are equivalent if the merkle hash of their subtrees is equal.

    Apply the merkle function to both trees, and then do a DFS, which simply checks if the merkle hash of the current nodes are the same,
    and if not, calls the function recursively on the left and right nodes of s, and sees if any of these recursive calls return True.

    Time Complexity: O(s+t), since we simply iterate through each tree once to create the merkle hashes, and once more through s to check
    if there is an identical subtree.
    Space Complexity:O(h_s)
    '''
    def isSubtree(self, s, t):
        from hashlib import sha256
        def hash_(x):
            S = sha256()
            S.update(x)
            return S.hexdigest()
            
        def merkle(node):
            if not node:
                return '#'
            m_left = merkle(node.left)
            m_right = merkle(node.right)
            node.merkle = hash_(m_left + str(node.val) + m_right)
            return node.merkle
            
        merkle(s)
        merkle(t)
        def dfs(node):
            if not node:
                return False
            return (node.merkle == t.merkle or dfs(node.left) or dfs(node.right))
        return dfs(s)