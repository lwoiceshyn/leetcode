'''
https://leetcode.com/problems/binary-tree-postorder-traversal/
'''

class Solution:
    '''
    If you analyze the pattern of the postorder traversal, you'll notice that the reverse of the postorder
    is actually the reverse preorder traversal (root right left). Simply use a stack for the 
    iterative reverse preorder traversal, and then reverse the the output. For iterative approach,
    append the left before the right to the stack so the right gets processed before left.

    Time Complexity: O(n)
    Space Complexity: O(h)
    
    Example:
            6
           /  \
          3    7
         / |  / \
        2  1 4   5
      
    Preorder: 6 3 2 1 7 4 5
    Postorder: 2 1 3 4 5 7 6
    Reverse Postorder: 6 7 5 4 3 1 2  (As if we we're doing Preorder but with left and right swapped)
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