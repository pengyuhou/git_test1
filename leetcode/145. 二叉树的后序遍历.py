# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        ret=[]
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            dfs(node.right)
            ret.append(node.val)
        dfs(root)
        return ret






