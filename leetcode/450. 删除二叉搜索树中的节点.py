# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        if root.val == key:
            ret = []
            cur = root
            queue = [cur]
            while queue:
                a = queue.pop(0)
                ret.append(a.val)
                if a.left:
                    queue.append(a.left)
                if a.right:
                    queue.append(a.right)
            ret.remove(cur.val)
            res = sorted(ret)
            tmp = TreeNode(-1)
            tx = tmp
            while res:
                tmp.left = TreeNode(res.pop())
                tmp = tmp.left
            root = tx.left
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        return root
