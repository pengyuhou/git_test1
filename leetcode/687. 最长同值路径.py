# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left and root.right:
            if root.val == root.right.val and root.val != root.left.val:
                return max(self.longestUnivaluePath(root.left), self.longestUnivaluePath(root.right) + 1)
            if root.val == root.left.val and root.val != root.right.val:
                return max(self.longestUnivaluePath(root.left) + 1, self.longestUnivaluePath(root.right))
            if root.val == root.right.val and root.val == root.left.val:
                return self.longestUnivaluePath(root.left) + self.longestUnivaluePath(root.right)
            return max(self.longestUnivaluePath(root.left), self.longestUnivaluePath(root.right))
        if root.left and not root.right:
            if root.val == root.left.val:
                return self.longestUnivaluePath(root.left) + 1
            else:
                return self.longestUnivaluePath(root.left)
        if root.right and not root.left:
            if root.val == root.right.val:
                return self.longestUnivaluePath(root.right) + 1
            else:
                return self.longestUnivaluePath(root.right)
        if not root.right and not root.left:
            return 0
