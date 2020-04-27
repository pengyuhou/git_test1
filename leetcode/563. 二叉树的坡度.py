# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if not root:
            return 0
        def fun(node):
            if not node:
                return 0
            return fun(node.left) + fun(node.right) + node.val
        return self.findTilt(root.left) + self.findTilt(root.right) + abs(fun(root.left) - fun(root.right))




