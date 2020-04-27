# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        ret = [root.val]

        def dfs(node):
            if not node.left and not node.right:
                return

            if node.left:
                ret.append(node.left.val)
                dfs(node.left)
            if node.right:
                ret.append(node.right.val)
                dfs(node.right)

        dfs(root)
        ret = ret[1:]
        while ret:
            root.left = None
            root.right = TreeNode(ret.pop(0))
            root = root.right
