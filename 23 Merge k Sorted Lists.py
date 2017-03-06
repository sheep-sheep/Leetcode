import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        pq = []
        for head in lists:
            if head:
                heapq.heappush(pq, (head.val, head))
        dummpy = ListNode(0)
        start = dummpy
        while(pq):
            curr = heapq.heappop(pq)[1]
            start.next = curr
            start = start.next
            if curr.next:
                curr = curr.next
                heapq.heappush(pq, (curr.val, curr))
        return dummpy.next
