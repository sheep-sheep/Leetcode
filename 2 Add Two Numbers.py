# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def convertLLtoList(self, L):
        tmp = []
        while(L.next != None):
            tmp.append(L.val)
            L = L.next
        return tmp
        
    def creatLLfromList(self, l):
        if len(l) == 1:
            return ListNode(l[0])
        else:
            node = ListNode(l[-1])
            node.next = self.creatLLfromList(l[:-1])
            return node
            
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        l1 = self.convertLLtoList(l1)
        l2 = self.convertLLtoList(l2)
        
        if len(l1) < len(l2):
            A = l1
            B = l2
        else:
            A = l2
            B = l1
        i = e = 0 
        c = []
        for a in A:
            b = B[i]
            i = i+1
            if a + b + e < 10:
                c.append(a + b + e)
                e = 0
            else:
                c.append(a + b + e - 10)
                e = 1
                
        for b in B[i:]:
            i = i + 1
            if b + e < 10:
                c.append(b)
            else:
                c.append(b+e-10)
                e = 1
        
        if e == 1:
            c.append(e)
        
        result = self.creatLLfromList(c)
        
        return result
        
        

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution_2(object):
    
    def convertLLtoList(self, L):
        tmp = []
        while(L.val != None):
            tmp.append(L.val)
            if L.next != None:
                L = L.next
            else:
                break
        return tmp
        
    def convertListtoNum(self, nums):
        count = 0
        result = 0
        for num in nums:
            result = result + num * 10**count
            count = count + 1
        return result
        
    def creatLLfromList(self, l):
        if len(l) == 1:
            return ListNode(l[0])
        else:
            node = ListNode(l[-1])
            node.next = self.creatLLfromList(l[:-1])
            return node

    def addTwoNumbers(self, l1, l2):
        l1_num = self.convertListtoNum(self.convertLLtoList(l1))
        l2_num = self.convertListtoNum(self.convertLLtoList(l2))
        result = l1_num + l2_num 
        result_list = [int(i) for i in list(str(result))]
        return self.creatLLfromList(result_list)
        
        
