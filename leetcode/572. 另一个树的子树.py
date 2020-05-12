# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def fun(self, u, v):
        if not u and not v:
            return True
        return u and v and u.val == v.val and self.fun(u.left, v.left) and self.fun(u.right, v.right)

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        if not s and not t:
            return True
        if (not s and t) or (not t and s):
            return False
        return self.fun(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


class Solution1:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def fun(x, y):
            if not x and not y:
                return True
            if (not x and y) or (not y and x):
                return False
            return x.val == y.val and fun(x.left, y.left) and fun(x.right, y.right)

        if not s and not t:
            return True
        if (not s and t) or (not t and s):
            return False
        return fun(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


if __name__ == "__main__":
    pass
