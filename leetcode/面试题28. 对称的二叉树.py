# # Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = [root]
        ret = [[root.val]]
        while queue:
            l = len(queue)
            tmp = []
            for _ in range(l):
                a = queue.pop(0)
                if a:
                    tmp.append(a.val)
                else:
                    tmp.append(None)
                if a:
                    queue.append(a.left)
                    queue.append(a.right)
            ret.append(tmp)
        for i in range(len(ret)):
            tmp = ret[i].copy()
            ret[i].reverse()
            if tmp!=ret[i]:
                return False
        return True





















