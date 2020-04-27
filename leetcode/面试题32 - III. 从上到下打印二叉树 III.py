# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) :
        if not root:
            return []
        queue = [root]
        index = 1
        ret =[]
        while queue:
            l = len(queue)
            tmp = []
            for _ in range(l):
                a = queue.pop(0)
                tmp.append(a.val)

                if a.left:
                    queue.append(a.left)
                if a.right:
                    queue.append(a.right)
            if not index%2:
                tmp.reverse()
            ret.append(tmp)
            index += 1
        return ret









