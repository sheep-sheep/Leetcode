# It's by my own!!!!!
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def checkSymmetric(p, q):
            if p is None and q is None:
                return True
            if p and q and p.val == q.val:
                return checkSymmetric(p.left, q.right) and checkSymmetric(p.right, q.left)
            else:
                return False
                
        if not root:
            return True
        return checkSymmetric(root.left, root.right)
# TODO: DO it iteratively!!!

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        pre = []
        post = []
        self.preOrder(root, pre)
        self.postOrder(root, post)
        if len(pre)!= len(post):
            return False
        else:
            print pre
            print post
            for count in range(len(pre)):
                if pre[count]!=post[count]:
                    return False
            return True
    
    def preOrder(self, root, res):
        if root and root.left:
            self.preOrder(root.left, res)
        if root:
            res.append(root.val)
        else:
            res.append(None)
        if root and root.right:
            self.preOrder(root.right, res)
    
    def postOrder(self, root, res):
        if root and root.right:
            self.postOrder(root.right, res)
        if root:
            res.append(root.val)
        else:
            res.append(None)
        if root and root.left:
            self.postOrder(root.left, res)
