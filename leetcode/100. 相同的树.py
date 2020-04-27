# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p and q:
            return False
        if not q and p:
            return False
        def fun(node, ret):
            queue = [node]
            while True:
                l = len(queue)
                tmp = []
                res = []
                for _ in range(l):
                    a = queue.pop(0)
                    if not a:
                        tmp.append(None)
                        tmp.append(None)
                        res.append(None)
                    else:
                        res.append(a.val)
                        if a.left:
                            tmp.append(a.left)
                        else:
                            tmp.append(None)
                        if a.right:
                            tmp.append(a.right)
                        else:
                            tmp.append(None)
                if all([i is None for i in res]):
                    ret.append(res)
                    break
                else:
                    queue = tmp[:]
                    ret.append(res)
        ret1 = []
        ret2 = []
        fun(p,ret1)
        fun(q,ret2)
        print(ret1)
        print(ret2)
        return ret1==ret2
