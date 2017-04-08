# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
            
        dummy = ListNode(0)
        dummy.next = head
        start = dummy.next
        fast = start.next
        
        while(fast):
            if start.val != fast.val:
                start = fast
                fast = fast.next
            else:
                start.next = fast.next
                fast = fast.next
        
        return dummy.next
