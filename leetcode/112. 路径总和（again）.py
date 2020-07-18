# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
# class Solution(object):
#     def hasPathSum(self, root, s):
#         if not root:
#             return False
#         ret = []
#
#         def dfs(node, res):
#             if not node.left and not node.right:
#                 ret.append(res.copy())
#                 return
#             if node.left:
#                 res.append(node.left.val)
#                 dfs(node.left, res)
#                 res.pop()
#             if node.right:
#                 res.append(node.right.val)
#                 dfs(node.right, res)
#                 res.pop()
#
#         dfs(root, [root.val])
#         return any([sum(i) == s for i in ret])


class Solution(object):
    def hasPathSum(self, root, s):
        if not root:
            return False

        def dfs(node, res):
            if not node.left and not node.right:
                if sum(res) == s:
                    return True
                else:
                    return False
            x1 = None
            x2 = None
            if node.left:
                res.append(node.left.val)
                x1 = dfs(node.left, res)
                res.pop()
            if node.right:
                res.append(node.right.val)
                x2 = dfs(node.right, res)
                res.pop()
            if x1 or x2:
                return True
            else:
                return False
        return dfs(root, [root.val])
