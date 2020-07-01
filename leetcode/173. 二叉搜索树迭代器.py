# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:
    ret = []

    def __init__(self, root: TreeNode):
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.ret.append(node.val)
            dfs(node.right)

        dfs(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.ret.pop(0)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return bool(self.ret)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

print(any([0, 0]))
