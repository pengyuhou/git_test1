# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        count = 0
        ret = []
        def dfs(node,count):
            if not node:
                ret.append(count)
                return

            dfs(node.left,count+1)
            dfs(node.right,count+1)
        dfs(root,count)
        return max(ret)






















