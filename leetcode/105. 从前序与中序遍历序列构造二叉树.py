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
        a = TreeNode(preorder[0])

        index = inorder.index(preorder[0])

        pre_left = preorder[1:index+1]
        pre_right = preorder[index+1:]
        in_left = inorder[:index]
        in_right = inorder[index+1:]

        a.left = self.buildTree(pre_left,in_left)
        a.right = self.buildTree(pre_right,in_right)
        return a