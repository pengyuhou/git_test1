# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if not root.left and not root.right:
            if val > root.val:
                root.right = TreeNode(val)

            else:
                root.left = TreeNode(val)
            return root
        if root.left and not root.right:
            if val < root.val:
                root.left = self.insertIntoBST(root.left, val)
            else:
                root.right = TreeNode(val)
            return root
        if root.right and not root.left:
            if val < root.val:
                root.left = TreeNode(val)
            else:
                root.right = self.insertIntoBST(root.right, val)
            return root

        if root.left and root.right:
            if val < root.val:
                root.left = self.insertIntoBST(root.left, val)
            else:
                root.right = self.insertIntoBST(root.right, val)
            return root
# class Solution:
#     def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
#         ret = []
#         def dfs(node):
#             if not node:
#                 return
#             dfs(node.left)
#             ret.append(node.val)
#             dfs(node.right)
#         ret.append(val)
#         ret.sort()
#         a = TreeNode(-1)
#         tmp = a
#         while ret:
#             a.right = TreeNode(ret.pop(0))
#             a = a.right
#         return tmp
