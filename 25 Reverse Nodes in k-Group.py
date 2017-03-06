class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        pointer0 = head
        pointer1 = head.next if head else None
        for i in range(k - 2):
            pointer1 = pointer1.next if pointer1 else None
        while(pointer0 and pointer1):
            start.next = pointer1
            pointer0.next = pointer1.next
            pointer1.next = pointer0


            for i in range(k):
                start = start.next
            pointer0 = start.next
            pointer1 = start.next
            for i in range(k - 2):
                pointer1 = pointer1.next if pointer1 else None
        return dummy.next

    def reverse(self, p0, p1, k):
        return p0, p1
