# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        if not nums:
            return
        l = len(nums)
        mid = l // 2
        a = TreeNode(nums[mid])
        a.left = self.sortedArrayToBST(nums[:mid])
        a.right = self.sortedArrayToBST(nums[mid + 1:])
        return a

