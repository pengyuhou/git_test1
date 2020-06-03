# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ret = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            ret.append(node.val)
            dfs(node.right)

        dfs(root)
        a = TreeNode(-1)
        tmp = a
        while ret:
            a.right = TreeNode(ret.pop(0))
            a = a.right
        return tmp.right
