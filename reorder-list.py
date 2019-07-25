'''
https://leetcode.com/problems/reorder-list/
'''

class Solution(object):
    def reorderList(self, head):
        """
        This solution works as follows: First, split the list into two halves. Then, reverse the second half. Then, merge the two halves alternating between the first
        and second half. Since all of these are O(n), the full algorithm is linear.

        Splitting the list into two halves: This is done by finding the center of the list using the two-pointer tortoise-and-hare method, where the slow pointer 
        will point to the center of the linked list when the fast pointer reaches the end. Once found, the node prior to the middle node is set to point to None.

        Reversing the second half: Simply iterative linked list reversal (see reverse-linked-list.py)

        Merging the two halves: Assign a current pointer to a dummy node, then go through each half linked list we created earlier. Point current to the next node
        in the first half and advance it by one, and then repeat for the second half until both lists have been finished except for the last value, and then add
        the last value (which will occur when either half has reached the end).

        Note: This problem asks for no return value and rather to modify in-place so that head points to the desired reordered list.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not head or not head.next:
            return head 
        slow, fast, prev = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = None

        prev, curr = None, slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        curr = ListNode(0)
        l1,l2 = head, prev
        while l1 and l2:
            curr.next = l1
            l1 = l1.next
            curr = curr.next
            curr.next = l2
            l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2