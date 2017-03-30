# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        elif not head.next:
            return head
        else:
            pointer = head
            length = 1
            while pointer.next:
                pointer = pointer.next
                length += 1
            dummy = ListNode(0)
            dummy.next = head
            slow = dummy
            fast = dummy
            for _ in range(k%length):
                if fast.next:
                    fast = fast.next
                else:
                    fast = dummy
            while(fast.next!=None):
                fast = fast.next
                slow = slow.next
            fast.next = head
            dummy.next = slow.next
            slow.next = None
            return dummy.next
        
        
