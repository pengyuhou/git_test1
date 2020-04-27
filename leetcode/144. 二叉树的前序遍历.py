# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):


    def preorderTraversal(self, root):
        if root is None:
            return []
        ret=[]
        def dfs(node):
            if node is None:
                return
            ret.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ret