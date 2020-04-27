# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, target):

        if not root:
            return []
        ret = []
        def dfs(node,res):
            if not node.left and not node.right:
                if sum(res)==target:
                    ret.append(res.copy())
                return
            if node.left:
                res.append(node.left.val)
                dfs(node.left,res)
                res.pop()
            if node.right:
                res.append(node.right.val)
                dfs(node.right,res)
                res.pop()
        dfs(root,[root.val])
        return ret

















