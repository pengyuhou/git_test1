# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
class Solution {
    public int pathSum(TreeNode root, int sum) {
        if(root == null){
            return 0;
        }
        int result = countPath(root,sum);
        int a = pathSum(root.left,sum);
        int b = pathSum(root.right,sum);
        return result+a+b;

    }
    public int countPath(TreeNode root,int sum){
        if(root == null){
            return 0;
        }
        sum = sum - root.val;
        int result = sum == 0 ? 1:0;
        return result + countPath(root.left,sum) + countPath(root.right,sum);
    }
}
"""


class Solution:
    def pathSum(self, root: TreeNode, s: int) -> int:
        def dfs(node, val):
            if not node:
                return 0
            val -= node.val
            if val == 0:
                ret = 1
            else:
                ret = 0
            return ret + dfs(node.left, val) + dfs(node.right, val)

        if not root:
            return 0
        res = dfs(root, s)
        a = self.pathSum(root.left, s)
        b = self.pathSum(root.right, s)
        return res + a + b
