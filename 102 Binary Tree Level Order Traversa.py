# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        from Queue import Queue
        q = Queue()
        res, final= [],[]
        q.put(root)
        while(not q.empty()):
            n = q.qsize()
            while n:
                node = q.get()
                if node.left:
                    q.put(node.left)
                res.append(node.val)
                if node.right:
                    q.put(node.right)
                n -= 1
            final.append(res)
            res = []
        return final
