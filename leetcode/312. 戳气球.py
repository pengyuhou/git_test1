class Solution(object):
    def maxCoins(self, nums):
        import functools
        @functools.lru_cache(None)
        def dfs(p):
            if not p:
                return 0
            if len(p) == 1:
                return p[0]
            ret = -float('inf')
            for i in range(len(p)):
                if i == 0:
                    val = p[0] * p[1]
                    ret = max(ret, dfs(p[i + 1:]) + val)
                elif i == len(p) - 1:
                    val = p[-1] * p[-2]
                    ret = max(ret, dfs(p[:i]) + val)
                else:
                    val = p[i] * p[i - 1] * p[i + 1]
                    ret = max(ret, dfs(p[:i] + p[i + 1:]) + val)
            return ret

        return dfs(tuple(nums))


if __name__ == "__main__":
    print(Solution().maxCoins([8, 3, 4, 3, 5, 0, 5, 6, 6, 2, 8, 5, 6, 2, 3, 8, 3, 5, 1, 0, 2]))
