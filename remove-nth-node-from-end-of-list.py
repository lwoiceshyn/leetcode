'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

'''


class Solution(object):
	'''
	One-pass solution using two pointers.

	Create two pointers, called behind and ahead. Behind will attempt to lag ahead by n nodes, meaning that the node we are trying to remove is the node that behind will be pointing to,
	since if we want to remove the node 2 from the end of a list of length 5, we are removing the 4th node. Initially, point behind and ahead to the function's passed in head. Then,
	advance ahead n times. In the case where we want to remove the first node, n will be equal to the length of the list, and ahead will have advanced past the last node in the list,
	and be pointing to None. We first check if ahead is pointing to None. In this case, the passed in list is either length 1, or length >1. If length is >1, then behind.next will be a legitimate
	node, and we are only trying to remove the first node, which behind is pointing to, so we can simply return behind.next, which is the second node of the list. If length == 1, then behind.next
	will be None, and we know that we're removing the only node in a list of length 1, so we return None.

	If ahead is not pointing to None, then this means we are not trying to remove the first node. In this case, we want to keep advancing ahead until it reaches the last node, in which case ahead.next
	is None, which is the condition that breaks this while loop. We also want to increment behind every time we increment ahead. Finally, once ahead reaches the last node, we simply re-assign behind.next
	to behind.next.next, removing this node from the list.

	Time Complexity: O(n)
	Space Complexity: O(1)
	'''
    def removeNthFromEnd(self, head, n):
        ahead = behind = head
        for _ in range(n):
            ahead = ahead.next
        if not ahead:
            if behind.next:
                return behind.next
            else:
                return None
        while ahead.next:
            ahead = ahead.next
            behind = behind.next
        behind.next = behind.next.next
        return head