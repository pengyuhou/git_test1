# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         def recur(node1, node2):
#             if not node1 and not node2:
#                 return True
#             if not node1 or not node2:
#                 return False
#             return node1.val == node2.val and recur(node1.left, node2.right) and recur(node1.right, node2.left)
#         return recur(root, root)


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def ishuiwen(p):
            index1 = 0
            index2 = len(p) - 1
            while index1 < len(p) and index2 >= 0 and p[index1] == p[index2]:
                index1 += 1
                index2 -= 1
            if index2 > index1:
                return False
            else:
                return True
        if not root:
            return True
        from collections import deque
        d = deque([root])
        ret = []
        while d:
            tmp = []
            for _ in range(len(d)):
                a = d.popleft()
                if not a:
                    tmp.append(None)
                    continue
                else:
                    tmp.append(a.val)
                if a.left:
                    d.append(a.left)
                else:
                    d.append(None)
                if a.right:
                    d.append(a.right)
                else:
                    d.append(None)
            ret.append(tmp)
        return all([ishuiwen(i) for i in ret])
