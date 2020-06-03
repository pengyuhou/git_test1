# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return
        if root.val == val:
            return root
        a = self.searchBST(root.left, val)
        b = self.searchBST(root.right, val)
        if a:
            return a
        if b:
            return b
