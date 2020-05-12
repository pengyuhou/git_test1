# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        if (root.left == p and root.right == q) or root == p or root == q:
            return root
        val_left = self.lowestCommonAncestor(root.left, p, q)
        val_right = self.lowestCommonAncestor(root.right, p, q)
        if val_left and val_right:
            return root
        if val_left:
            return val_left
        if val_right:
            return val_right

