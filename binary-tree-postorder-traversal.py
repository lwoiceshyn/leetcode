'''
https://leetcode.com/problems/binary-tree-postorder-traversal/
'''

class Solution:
    '''
    If you analyze the pattern of the postorder traversal, you'll notice that the reverse of the postorder
    is actually the reverse preorder traversal (root right left) in reverse. Simply use a stack for the 
    iterative reverse preorder traversal, and then reverse the the output.

    Time Complexity: O(n)
    Space Complexity: O(h)
    '''
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        res = []
        while stack and root:
            root = stack.pop()
            res.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return res[::-1]