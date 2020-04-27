# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        queue = [root]
        ret=[]
        while queue:
            tmp=[]
            l = len(queue)
            for _ in range(l):
                a=queue.pop(0)
                tmp.append(a.val)
                if a.left:
                    queue.append(a.left)
                if a.right:
                    queue.append(a.right)
            ret.append(sum(tmp)/l)
        return ret


















