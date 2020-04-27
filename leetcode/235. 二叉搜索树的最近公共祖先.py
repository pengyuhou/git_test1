# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        root_val = root.val
        p_val =p.val
        q_val = q.val
        if p_val<root_val and q_val<root_val:
            self.lowestCommonAncestor(root.left,p,q)
        if p_val>root_val and q_val>root_val:
            self.lowestCommonAncestor(root.right,p,q)
        else:
            return root
