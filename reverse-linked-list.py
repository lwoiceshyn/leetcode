'''
https://leetcode.com/problems/reverse-linked-list/
'''


class Solution:
	'''
	Iterative reversal. Stores a temporary pointer to the next node, points the current node to the previous node, then assigns the previous node pointer 
	to the current node, and the current node pointer to the temporary pointer. Continue this loop until the current pointer is pointing to None, e.g.,
	we reached the end of the linked list. Then return the node the previous pointer is referring to, as this will be the new head.

	Time Complexity: O(n)
	Space Complexity: O(1)
	'''
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        prev = None
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev

class Solution:
	'''
	Recursive reversal. The first if statement checks if an empty list has been passed in or not. If not, use a temporary pointer to the next node, point the current node to the 
	passed-in tail. Then, check for the base case: the temporary pointer is pointing to None. If met, return head, else, recursively call the function with the temporary pointer
	as head, and the current head as tail.

	Time Complexity: O(n)
	Space Complexity: O(n)
	'''
    def reverseList(self, head: ListNode, tail=None) -> ListNode:
        if not head:
            return None
        next_temp = head.next
        head.next = tail
        if not next_temp:
            return head
        else:
            return self.reverseList(next_temp, head)