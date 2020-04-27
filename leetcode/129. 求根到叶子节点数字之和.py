# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        ret = []
        def dfs(node,res):
            if not node.left and not node.right:
                ret.append(int(''.join([str(i) for i in res.copy()])))
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
        return sum(ret)
























