"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        ret = []
        def dfs(node):
            if node is None:
                return
            for child in node.children:
                dfs(child)
            ret.append(node.val)
        dfs(root)
        return ret







