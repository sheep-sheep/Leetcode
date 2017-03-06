# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        pointer0 = head
        pointer1 = head.next if head else None
        while(pointer0 and pointer1):
            start.next = pointer1
            pointer0.next = pointer1.next
            pointer1.next = pointer0
            start = start.next.next
            pointer0 = start.next
            pointer1 = start.next
            pointer1 = pointer1.next if pointer1 else None

        return dummy.next
