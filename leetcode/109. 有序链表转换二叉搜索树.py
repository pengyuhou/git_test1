# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        cur1 = head
        ret = []
        while cur1:
            ret.append(cur1.val)
            cur1 = cur1.next
        def recursion(nums):
            if not nums:
                return
            l = len(nums)
            mid = l//2
            node = TreeNode(nums[mid])
            node.left = recursion(nums[:mid])
            node.right = recursion(nums[mid+1:])
            return node
        return recursion(ret)












