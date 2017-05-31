class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def depth(height, root):
            if root:
                return max(depth(height+1, root.left), depth(height+1, root.right))
            return height
        if root:
            left = depth(1, root.left)
            right = depth(1, root.right)
            return abs(left-right)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        return True
        
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def height(root):
            if not root:
                return 0
            leftheight = height(root.left)
            rightheight = height(root.right)
            if leftheight is None or rightheight is None:
                return None
            if abs(leftheight-rightheight)>1:
                return None
            return max(leftheight, rightheight)+1
        return height(root) is not None        
