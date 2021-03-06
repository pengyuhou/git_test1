
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        ret = []
        def dfs(node):
            if node is None:
                return
            ret.append(node.val)
            for child in node.children:
                dfs(child)
        dfs(root)
        return ret







