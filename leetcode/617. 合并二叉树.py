# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return
        if t1 and t2:
            a = TreeNode(t1.val + t2.val)
            a.left = self.mergeTrees(t1.left, t2.left)
            a.right = self.mergeTrees(t1.right, t2.right)
        if t1 and not t2:
            a = TreeNode(t1.val)
            a.left = self.mergeTrees(t1.left, None)
            a.right = self.mergeTrees(t1.right, None)
        if not t1 and t2:
            a = TreeNode(t2.val)
            a.left = self.mergeTrees(None, t2.left)
            a.right = self.mergeTrees(None, t2.right)
        return a
