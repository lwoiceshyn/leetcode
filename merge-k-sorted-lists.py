'''
https://leetcode.com/problems/merge-k-sorted-lists/
'''

class Solution:
    '''
    Divide and conquer solution. Since merging two sorted linked lists is trivial, and the time complexity is O(n), we can divide
    our list of lists into halves until we have all pairs of them only, and then merge each pair together in linear time. Dividing
    our list only takes log(k) time, so the total time complexity is O(nklog(k)).

    Time Complexity: O(nklog(k)), where n is the length of the longest linked list, and k is the number of linked lists.
    Space Complexity: O(1)
    '''
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or not any(lists):
            return None
        if len(lists) == 1:
            return lists[0]
        
        return self.divideConquerLists(lists, start=0, end=len(lists)-1)
    
    def merge2Lists(self, l1, l2):
        dummy = curr = ListNode(0)
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

    def divideConquerLists(self, lists, start, end):
        if start+1 < end:
            mid = (start + end) // 2
            head1 = self.divideConquerLists(lists, start, mid)
            head2 = self.divideConquerLists(lists, mid+1, end)
            return self.merge2Lists(head1, head2)
        elif start+1 == end: #two lists left
            return self.merge2Lists(lists[start], lists[end])    
        elif start == end: # one list left
            return lists[start]

class Solution2:
    '''
    Naive recursive solution. Each function call causes an iteration through all of the passed in lists, finding the minimum node value amongst them.
    Then, this value's new next value is assigned to the recursive call of the set of lists with this node set to its next value. A checking loop
    is used to eliminate all of the null lists each function call.

    Time Complexity: O(nk^2), since there are n*k total recursive calls, and each recursive call loops through each linked list.
    Space Complexity: O(1)

    '''
    def mergeKLists(self, lists):
        if not lists or not any(lists):
            return None
        if len(lists) == 1:
            return lists[0]
        return self.recurse(lists)

    def recurse(self, lists):
        if len(lists) == 1:
            return lists[0]
        del_indices = []
        for i, l in enumerate(lists):
            if not l:
                del_indices.append(i)
        for index in sorted(del_indices, reverse=True):
            del lists[index]
        min_val = lists[0].val
        min_head = lists[0]
        min_idx = 0
        for i, l in enumerate(lists):
            if l.val < min_val:
                min_val = l.val
                min_head= l
                min_idx = i
        lists[min_idx] = lists[min_idx].next
        min_head.next = self.recurse(lists)
        return min_hea


