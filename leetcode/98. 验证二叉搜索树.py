# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        ret = []
        def dfs(node):
            if not node:
                return
            mid_val = node.val
            dfs(node.left)
            ret.append(mid_val)
            dfs(node.right)
        dfs(root)
        if sorted(ret)==ret:
            return True
        else:
            return False








