# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum_val):
        if not root:
            return []
        ret =[]
        def dfs(node,res):
            if node.left == None and node.right==None and node != None:
                res.append(node.val)
                if sum(res)==sum_val:
                    ret.append(res.copy())
                return
            res.append(node.val)
            dfs(node.left, res)
            dfs(node.right,res)
            res.pop()

        dfs(root,[])
        return ret







