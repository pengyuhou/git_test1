# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        if not root:
            return ''
        a = enumerate('abcdefghijklmnopqrstuvwxyz')

        a = map(lambda x: [str(x[0]), x[1]], a)
        key = {i: j for i, j in list(a)}

        ret = []

        def dfs(node, res):
            if not node.left and not node.right:
                tmp = []
                for i in res:
                    tmp.append( key[str(i)] )
                ret.append(tmp)
                return

            if node.left:
                res.append(str(node.left.val))
                dfs(node.left, res)
                res.pop()
            if node.right:
                res.append(str(node.right.val))
                dfs(node.right, res)
                res.pop()

        dfs(root, [root.val])
        for i in range(len(ret)):
            ret[i].reverse()
            ret[i] = ''.join(ret[i])


        return sorted(ret)[0]


# print(Solution().smallestFromLeaf())

