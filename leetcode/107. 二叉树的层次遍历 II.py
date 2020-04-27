# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = [root]
        ret = []
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
            ret.append(tmp)
        ret.reverse()
        return ret

a=[1,2,3,4,5]
a[2:]=[5,6]
print(a)










