# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return
        mid = inorder.index(preorder[0])
        a = TreeNode(preorder[0])
        a.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        a.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return a
