class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        helper = dict()
        dummy = RandomListNode(0)
        dummy.next = head
        
        while head:
            helper[head] = RandomListNode(head.label)
            head = head.next
        
        head = dummy.next
        
        while head:
            if head.next:
                helper[head].next = helper[head.next]
            if head.random:
                helper[head].random = helper[head.random]
            head = head.next
        
        return helper[dummy.next]
