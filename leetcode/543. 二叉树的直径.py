# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        def depth(node):
            if not node:
                return 0
            return max(depth(node.left), depth(node.right)) + 1
        return max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right),depth(root.left) + depth(root.right))
        

