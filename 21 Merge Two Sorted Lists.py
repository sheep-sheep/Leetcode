class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        starter = ListNode(0)
        pointer = starter
        pointer1 = l1
        pointer2 = l2
        if l1 is None and l2:
            return l2
        elif l2 is None and l1:
            return l1
        elif l1 is None and l2 is None:
            return None
        else:
            while(pointer1 and pointer2):
                if pointer1.val <= pointer2.val:
                    pointer.next = pointer1
                    pointer1 = pointer1.next
                else:
                    pointer.next = pointer2
                    pointer2 = pointer2.next
                pointer = pointer.next
            if pointer1:
                pointer.next = pointer1
            if pointer2:
                pointer.next = pointer2
            return starter.next
