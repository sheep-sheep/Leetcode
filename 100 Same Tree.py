# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def preOrder(root, res):
            res.append(root.val)
            if root.left:
                preOrder(root.left, res)
            if root.right:
                preOrder(root.right, res)
    
        res1, res2 = [], []
        preOrder(p, res1)
        preOrder(q, res2)
        
        if len(res1)!= len(res2):
            return False
        elif (not p) and (not q):
            return True
        else:
            print p 
            print q
            count = 0
            for res in res1:
                if res != res2[count]:
                    return False
            count +=1
        return True

                
