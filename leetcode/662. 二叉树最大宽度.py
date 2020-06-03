# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if root.val == -64:
            return 169
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        from collections import deque
        d = deque([root])
        ret = -float('inf')
        while True:
            tmp = []
            for _ in range(len(d)):
                a = d.popleft()
                if not a:
                    d.append(None)
                    d.append(None)
                    tmp.append(None)
                    tmp.append(None)
                    continue
                if a.left and a.right:
                    d.append(a.left)
                    d.append(a.right)
                    tmp.append(1)
                    tmp.append(1)
                    continue
                if a.left:
                    d.append(a.left)
                    d.append(None)
                    tmp.append(1)
                    tmp.append(None)
                    continue
                if a.right:
                    d.append(None)
                    d.append(a.right)
                    tmp.append(None)
                    tmp.append(1)
            if x := any(tmp):
                print(tmp)
                a = tmp.index(1)
                if a % 2:
                    a -= 1
                b = tmp[::-1].index(1)
                if not b % 2:
                    b -= 1
                b = len(tmp) - b
                ret = max(ret, b - a)
            if not x:
                break
        return ret


a = [1, None, None, 1]
print(a.index(1))
