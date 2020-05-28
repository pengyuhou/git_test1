# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums) -> TreeNode:
        if not nums:
            return
        index = nums.index(max(nums))
        left = nums[:index]
        right = nums[index + 1:]
        a = TreeNode(nums[index])
        a.left = self.constructMaximumBinaryTree(left)
        a.right = self.constructMaximumBinaryTree(right)
        return a



