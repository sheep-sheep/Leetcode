class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
                
        res = []
        self.preOrder(root, res)
        return res

    def preOrder(self, root, res):
        if root and root.left:
            self.preOrder(root.left, res)
        if root:
            res.append(root.val)
        if root and root.right:
            self.preOrder(root.right, res)
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack =[]
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right
