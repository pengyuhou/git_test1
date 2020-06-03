# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        ret = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            ret.append(node.val)
            dfs(node.right)

        dfs(root)
        index1 = 0
        index2 = len(ret) - 1
        if ret[index1] + ret[index2] < k:
            return False
        while index2 >= 0 and index1 < len(ret) and index1 < index2:
            if ret[index1] + ret[index2] == k:
                return True
            if ret[index1] + ret[index2] > k:
                index2 -= 1
            if ret[index1] + ret[index2] < k:
                index1 += 1

        return False
