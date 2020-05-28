"""
# Definition for a Node.

"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return
        from collections import deque
        d = deque([root])
        cnt = 0
        while d:
            for _ in range(len(d)):
                a = d.popleft()
                for child in a.children:
                    d.append(child)
            cnt += 1
        return cnt

import antigravity






























