# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return 0
        queue = [root]
        ret =[]
        while queue:
            a=queue.pop(0)
            ret.append(a.val)
            if a.left:
                queue.append(a.left)
            if a.right:
                queue.append(a.right)
        ret.sort()
        return ret[k-1]













