# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        queue = [root]
        ret = []
        while queue:
            a = queue.pop(0)
            ret.append(a.val)
            if a.left:
                queue.append(a.left)
            if a.right:
                queue.append(a.right)
        tmp = float('inf')
        ret.sort()
        for i in range(len(ret)-1):
            tmp = min(ret[i+1]-ret[i],tmp)
        return tmp




















