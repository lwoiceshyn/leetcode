'''
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

'''


class Codec:
	'''
	Here we utilize a double-ended queue (deque) to perform a breadth-first search of the current tree. If any node is None,
	we simply append a 'null' to our list of string representations of all of the values in the tree. If not, we append the
	string representation of the value, and add that nodes children to the deque. Thus, our final string will include only
	values in the tree and null values if they are children of non-null nodes. Thus, every level in the tree will be represented
	in order from top to bottom, left to right, with nulls only being represented if they are the child of a real node in the
	tree.

	In the deserialization process, we use a deque for all of the tree values, and a deque to process all of the necessary nodes
	in the tree. First, we make sure the root node isn't null and then populate our second deque with the root node. Then, we keep
	popping a node from our second deque, and if it's not null, pop two values from our first deque. For the non-null values in these,
	set the children of the current node to these two values, then append both to the second deque.


	Time Complexity: O(n)
	Space Complexity: O(n)

	'''
	from collections import deque
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        deck = deque([root])
        out = []
        while deck:
            node = deck.popleft()
            if not node:
                out.append('null')
            else:
                out.append(str(node.val))
                deck.append(node.left)
                deck.append(node.right)
        return ','.join(out)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = deque(data.split(','))
        root_val = vals.popleft()
        root = None if root_val == 'null' else TreeNode(int(root_val))
        deck = deque([root])
        while deck:
            node = deck.popleft()
            if node:
                l_val, r_val = vals.popleft(), vals.popleft()
                if l_val != "null":
                    node.left = TreeNode(int(l_val))
                if r_val != "null":
                    node.right = TreeNode(int(r_val))
                deck.append(node.left)
                deck.append(node.right)
        return root
