# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        ret = []
        def dfs(node,value):
            if not node.left and not node.right:
                ret.append(value)
                return 
            if node.left:
                dfs(node.left,node.left.val)
            if node.right:
                dfs(node.right,0)
        dfs(root,0)
        return sum(ret)












