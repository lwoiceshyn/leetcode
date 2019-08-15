'''
https://leetcode.com/problems/merge-two-sorted-lists/
'''

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        Iterative merging solution. First, check whether either or both input lists are empty and returns an appropriate output if any of these conditions are met. Then, assign two pointers to the 
        head of whichever list has a smaller head and advance its pointer by one. One pointer will be used to return the head of our new sorted list and the other will be used to construct the list.
        Then, iterate through each list simultaneously and add the lower value at each iteration as a subsequent node for the new list and advance its pointer by one, until either of the two lists
        are empty. Then, simply append whichever of the two lists is remaining to the end of the current new list, and return the head pointer that we made at the start.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if l1 and not l2:
            return l1
        elif l2 and not l1:
            return l2
        elif not l1 and not l2:
            return None
        if l1.val < l2.val:
            new = new_head =  l1
            l1 = l1.next
        else:
            new = new_head = l2
            l2 = l2.next
        while l1 and l2:
            if l1.val < l2.val:
                new.next = l1
                new = new.next
                l1 = l1.next
            else:
                new.next = l2
                new = new.next
                l2 = l2.next
        if l1:
            new.next = l1
        else:
            new.next = l2
        return new_head

class Solution2:
    def mergeTwoLists(self, l1, l2):
        """
        Iterative merging solution (from kamyu104 on github). Same as above, but uses a dummy node to make the code quite a bit cleaner. 
        The last line before the return is a nice way to assign a value when you know one of the two values is guaranteed to be None or False.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        curr = dummy = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next

class Solution3:
    def mergeTwoLists(self, l1, l2):
        """
        Recursive solution. If either of the passed in lists is None, return the other. Otherwise, check which value is smaller, assign the next value of that node
        to a recursive call on the next value of that node and the other lists' current node, then return that node. All of the returns in the recursion trace
        are just to end those respective calls, and only the first call of the function's return matters, which will return a pointer to the head of the minimum value
        between the two lists, which will now be restructured to point to the newly merged version.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if (l1.val < l2.val):
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2