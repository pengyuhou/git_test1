# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        if not root:
            return False
        ret = []
        def dfs(node,res):
            if not node.left and not node.right:
                if sum(res)==target:
                    ret.append(True)
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
        if ret:
            return True
        else:
            return False
























