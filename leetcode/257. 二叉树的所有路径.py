# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ret = []
        if not root:
            ret.append('')
            return ret
        ret = []

        def dfs(node, res):
            if not node.left and not node.right:
                ret.append('->'.join(res.copy()))
                return
            if node.left:
                res.append(str(node.left.val))
                dfs(node.left, res)
                res.pop()
            if node.right:
                res.append(str(node.right.val))
                dfs(node.right, res)
                res.pop()

        dfs(root, [str(root.val)])
        return ret


if __name__ == "__main__":
    pass