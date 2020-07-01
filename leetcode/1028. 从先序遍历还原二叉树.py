# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverFromPreorder(self, s: str):
        cnt = 0
        index = 0
        layers = []
        while index < len(s):
            if s[index] == '-':
                cnt += 1
            if s[index] != '-' and index != 0 and s[index - 1] == '-':
                layers.append(cnt)
                cnt = 0
            index += 1
        s = s.replace('-', ' ')
        res = s.split()
        res = list(map(int, res))
        layers.insert(0, 0)
        print(layers)
        print(res)
        mark = [False for _ in range(len(layers))]
        max_level = max(layers)

        def dfs(node, level):
            if level > max_level:
                return
            for i in range(len(layers)):
                if not mark[i] and layers[i] == level:
                    if not node.left:
                        node.left = TreeNode(res[i])
                        mark[i] = True
                        dfs(node.left, level + 1)
                    if not node.right:


print(Solution().recoverFromPreorder("1-2--3---4-5--6---7"))
