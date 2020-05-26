class Solution(object):
    count = 0
    def findTargetSumWays(self, nums, S):
        l = len(nums)
        def dfs(p, res, level):
            if level == l:
                if res == S:
                    self.count += 1
                return
            dfs(p[1:], res + p[0], level + 1)
            dfs(p[1:], res - p[0], level + 1)
        dfs(nums, 0, 0)
        return self.count


if __name__ == "__main__":
    print(Solution().findTargetSumWays([1, 1, 1, 1, 1],
                                       3))
