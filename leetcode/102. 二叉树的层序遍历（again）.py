# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return root
        queue = [root]
        ret = []
        while queue:
            tmp = []
            l = len(queue)
            for i in range(l):
                a = queue.pop(0)
                tmp.append(a.val)
                if a.left:
                    queue.append(a.left)
                if a.right:
                    queue.append(a.right)
            ret.append(tmp)
        return ret
