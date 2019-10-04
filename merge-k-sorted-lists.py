'''
https://leetcode.com/problems/merge-k-sorted-lists/
'''

class Solution:
    '''
    Divide and conquer solution. Since merging two sorted linked lists is trivial, and the time complexity is O(n), we can divide
    our list of lists into halves until we have all pairs of them only, and then merge each pair together in linear time. Dividing
    our list only takes log(k) time, so the total time complexity is O(nlog(k)).

    Time Complexity: O(nlog(k)), where n is the length of the longest linked list, and k is the number of linked lists.
    Space Complexity: O(log(k)), since we need recursive stack space for our divide and conquer.
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
        return min_head


import heapq
class Solution3:
    '''
    Use a min-heap as a priority queue to sort the linked lists in our list by their value. We do this using
    the heapq module, where we can have each item in the priority queue be represented by a tuple, where
    the first element in the tuple is the key, and the second is the object associated with that key, In this case,
    the key is the value of that linked list node, and the value is the node itself. First, assign dummy/curr nodes 
    in order to build/return the merged linked list, and create the priority queue out of all the nonempty lists.

    Then, while the priority queue isn't empty, extract the root, assign the next node in the merged list to this
    node, and then, if the root isn't a tail node, push its next node to the priority queue.

    Finally, when all nodes in the priority queue have been processed, i.e, reached their end, then return
    dummy, which is pointing to the head of the merged list.

    Time Complexity: O(nlog(k)), where n is the length of the longest list, and k is the number of linked lists. We need to traverse
                     at least n times, and our heap operations(push, pop) are botj log(k)
    Space Complexity: O(k), where k is the number of linked lists.
    '''
    def mergeKLists(self, lists):
        if not lists or not any(lists):
            return None
        if len(lists) == 1:
            return lists[0]
        dummy = curr = ListNode(0)
        pq = []
        for l in lists:
            if l:
                heapq.heappush(pq, (l.val, l))

        while pq:
            curr_min = heapq.heappop(pq)[1]
            curr.next = curr_min
            curr = curr.next
            if curr_min.next:
                heapq.heappush(pq, (curr_min.next.val, curr_min.next))
        return dummy.next


