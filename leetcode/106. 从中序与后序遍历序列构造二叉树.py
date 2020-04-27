# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return
        a = TreeNode(postorder[-1])

        index = inorder.index(postorder[-1])

        ord_left = inorder[:index]
        ord_right = inorder[index+1:]
        post_left = postorder[:index]
        post_right = postorder[index:-1]

        a.left = self.buildTree(ord_left,post_left)
        a.right = self.buildTree(ord_right,post_right)
        return a

