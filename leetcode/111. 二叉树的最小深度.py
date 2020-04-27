# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        count= 0
        while queue:
            l = len(queue)
            count += 1
            for _ in range(l):
                a = queue.pop(0)

                if not a.left and not a.right:
                    return count
                if a.left:
                    queue.append(a.left)
                if a.right:
                    queue.append(a.right)




























