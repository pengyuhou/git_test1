# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.count = 0
    def pathSum(self, root: TreeNode, s: int) -> int:
        if not root:
            return 0
        def dfs(node, res):
            if not node:
                if sum(res)==s:
                    self.count+=1
                return
            if node.right:
                dfs(node.right,[node.right.val])
                res.append(node.right.val)
                dfs(node.right, res)
                res.pop()
            if node.left:
                dfs(node.left,[node.left.val])
                res.append(node.left.val)
                dfs(node.left, res)
                res.pop()
        dfs(root, [root.val])
        return self.count
















