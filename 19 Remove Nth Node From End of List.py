# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        start = ListNode(0)
        slow = start
        fast = start
        slow.next = head

        for i in range(0, n+1):
            fast = fast.next

        while (fast != None):
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return start.next

head = ListNode(1)
head.next = ListNode(2)
print Solution().removeNthFromEnd(head, 1)
