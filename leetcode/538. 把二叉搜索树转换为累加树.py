# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    val = 0
    def convertBST(self, root):
        if not root:
            return
        self.convertBST(root.right)
        self.val += root.val
        root.val = self.val
        self.convertBST(root.left)
        return root

