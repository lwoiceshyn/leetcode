'''
https://leetcode.com/problems/https://leetcode.com/problems/linked-list-cycle/
'''


class Solution(object):
    def hasCycle(self, head):
        """
        Two-runner solution. Uses two pointers, slow and fast, which are incremented by different rates (1 vs 2) every iteration. If there is a loop,
        at some point, fast and slow will point to the same node, and we can return True.

        Note that we have to be careful to ensure that we are not calling next on a NoneType and that we can handle cases where the Linked List is either empty
        or only contains a single node.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        slow = fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

class Solution2(object):
    def hasCycle(self, head):
        """
        Hashing solution that simply stores previously visited nodes in a set and checks each node while traversing to see if it has already been visited.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        visited = set()
        curr = head
        while curr:
            if curr in visited:
                return True
            visited.add(curr)
            curr = curr.next
        return False