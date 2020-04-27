# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        ret = []
        count = 0
        while queue:
            l = len(queue)
            tmp = []
            for _ in range(l):
                a = queue.pop(0)
                tmp.append(a.val)
                if a.left:
                    queue.append(a.left)
                if a.right:
                    queue.append(a.right)
            if count%2:
                tmp.reverse()
                ret.append(tmp.copy())
            else:
                ret.append(tmp.copy())
            count += 1
        return ret

if __name__ == "__main__":
    a=[1,2,3,4,5]
    # a.reverse()
    print(a[5:1:-2])



