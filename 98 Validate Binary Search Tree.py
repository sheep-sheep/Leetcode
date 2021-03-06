class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        output = []
        self.inOrder(root, output)
        
        for i in range(1, len(output)):
            if output[i-1] >= output[i]:
                return False
        return True

    def inOrder(self, root, output):
        if root is None:
            return
        
        self.inOrder(root.left, output)
        output.append(root.val)
        self.inOrder(root.right, output)
        
        
# The reason to use a MIN and MAX is to help pass the previous min/max value to next level.
# If we don't have such infomation the BST order can't be valid.

# python max/min number: float('inf')/float('-inf')
