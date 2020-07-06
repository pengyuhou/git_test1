class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i]:
                break
            dp[0][i] = 1
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0]:
                break
            dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                if not obstacleGrid[i][j]:
                    if not obstacleGrid[i - 1][j] and not obstacleGrid[i][j - 1]:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                    elif not obstacleGrid[i - 1][j] and obstacleGrid[i][j - 1]:
                        dp[i][j] = dp[i - 1][j]
                    elif not obstacleGrid[i][j - 1] and obstacleGrid[i - 1][j]:
                        dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]


print(Solution().uniquePathsWithObstacles([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]))
