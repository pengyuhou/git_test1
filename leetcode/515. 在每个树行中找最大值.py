# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def largestValues(self, root: TreeNode):
        if not root:
            return
        from collections import deque
        d = deque([root])
        ret = []
        while d:
            tmp = []
            for _ in range(len(d)):
                a = d.popleft()
                tmp.append(a.val)
                if a.left:
                    d.append(a.left)
                if a.right:
                    d.append(a.right)
            ret.append(max(tmp))
        return ret


