# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        queue = [root]
        count = 0
        while queue:
            l = len(queue)
            count += 1
            for _ in range(l):
                a = queue.pop(0)
                if a.left:
                    queue.append(a.left)
                if a.right:
                    queue.append(a.right)
        return count
















