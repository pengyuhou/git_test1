# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(root,a):
            if not root:
                return 0
            if root in a.keys():
                return a[root]
            money = root.val
            if root.left:
                money += dfs(root.left.left,a) + dfs(root.left.right,a)
            if root.right:
                money += self.rob(root.right.left) + self.rob(root.right.right)
            res = max(money, dfs(root.left,a) + dfs(root.right,a))
            a[root] = res
            return res
        return dfs(root,{})



