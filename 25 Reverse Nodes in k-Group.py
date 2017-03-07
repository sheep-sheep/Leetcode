class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        curr = head
        count = 0
        # This part is to move the pointer
        while(curr != None and count != k):
            curr = curr.next
            count += 1
        if count == k:
            # This part is to divide the remaining question into subset
            curr = self.reverseKGroup(curr, k)
            # this part is actually reverse list
            while(count > 0):
                # Use 2 pointer to replace each other, this way it moves and replaces at the same time
                tmp = head.next
                head.next = curr
                curr = head
                head = tmp
                count -= 1
            head = curr
        return head
    
class Solution1(object):
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
