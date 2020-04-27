
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        ret = []
        while queue:
            tmp = []
            l = len(queue)
            for _ in range(l):
                a = queue.pop(0)
                tmp.append(a.val)
                for child in a.children:
                    if child is not None:
                        queue.append(child)
            ret.append(tmp)
        return ret














