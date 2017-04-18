class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def constructBST(left, right):
            trees = []
            for i in range(left, right+1):
                for leftNode in constructBST(left, i-1):
                    for rightNode in constructBST(i+1, right):
                        node = TreeNode(i)
                        node.left = leftNode
                        node.right = rightNode
                        trees += [node]
            return trees or [None]
        return constructBST(1, n) if n!=0 else []
