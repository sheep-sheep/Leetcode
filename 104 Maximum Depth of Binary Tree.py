class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        leftChildHeight=self.maxDepth(root.left)
        rightChildHeight=self.maxDepth(root.right)
        return max(leftChildHeight, rightChildHeight)+1
