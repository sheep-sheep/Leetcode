# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None

        leftDummy = ListNode(None)
        rightDummy = ListNode(None)
        leftNode, rightNode = leftDummy, rightDummy

        while(head.val != None):
            if head.val < x:
                leftNode.next = ListNode(head.val)
                leftNode = leftNode.next
            else:
                rightNode.next = ListNode(head.val)
                rightNode = rightNode.next
            if head.next:
                head = head.next
            else:
                break
        leftNode.next = rightDummy.next
        return leftDummy.next

def createList(elems):
    dummy = ListNode(None)
    node = dummy
    for elem in elems:
        node.next = ListNode(elem)
        node = node.next
    return dummy.next

def printList(head):
    while(head.val):
        print head.val
        if head.next:
            head = head.next
        else:
            break

# OMG, i feel this question is so easy and simple to implement.
# it took me 15 mins to finish. Must be a dream.

# 1. Sort and matain order and convert them into array and then combine
# 2. Traverse once and append to 2 list each time.

a = createList([])

b = Solution().partition(a, 6)

printList(b)
