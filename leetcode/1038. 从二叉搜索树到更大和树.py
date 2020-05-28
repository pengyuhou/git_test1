# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    sum_val = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        self.bstToGst(root.right)
        self.sum_val += root.val
        root.val = self.sum_val
        self.bstToGst(root.left)
        return root








