class Solution1(object):
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    dp[i][j] = max(1, 1 - dungeon[i][j])
                elif i == m - 1:
                    dp[i][j] = max(1, dp[i][j + 1] - dungeon[i][j])
                elif j == n - 1:
                    dp[i][j] = max(1, dp[i + 1][j] - dungeon[i][j])
                else:
                    dp[i][j] = max(1, min(dp[i + 1][j] - dungeon[i][j], dp[i][j + 1] - dungeon[i][j]))
        return dp[0][0]


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        import functools
        @functools.lru_cache(None)
        def dfs(x, y):
            ret = []
            for dx, dy in [(0, 1), (1, 0)]:
                if x + dx < m and y + dy < n:
                    ret.append(dfs(x + dx, y + dy))
            return max(1, min(ret) - dungeon[x][y]) if ret else max(1, 1 - dungeon[x][y])
        return dfs(0, 0)


if __name__ == "__main__":
    # print(Solution1().calculateMinimumHP([[-2, -3, 3]]))
    print(Solution().calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))
