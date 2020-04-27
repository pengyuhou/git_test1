# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        count = 1
        while queue:
            a = queue.pop(0)
            if a.left:
                queue.append(a.left)
                count += 1
            if a.right:
                queue.append(a.right)
                count += 1
        return count






















