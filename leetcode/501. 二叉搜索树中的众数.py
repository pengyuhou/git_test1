# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = [root]
        ret = []
        while queue:
            a = queue.pop(0)
            ret.append(a.val)
            if a.left:
                queue.append(a.left)
            if a.right:
                queue.append(a.right)
        a = {}
        for i in ret:
            if i not in a.keys():
                a[i] = 1
            else:
                a[i] += 1
        res = sorted(list(a.items()), key=lambda x: x[1])
        key = res[-1][1]
        ans = []
        for i in range(len(res) - 1, -1, -1):
            if res[i][1] == key:
                ans.append(res[i][0])
            else:
                break
        return ans

