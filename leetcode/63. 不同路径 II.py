class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1]==1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        res = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):

            if obstacleGrid[i][0] != 1:
                res[i][0] = 1
            else:
                break
        for j in range(n):

            if obstacleGrid[0][j] != 1:
                res[0][j] = 1
            else:
                break
        res[0][0] = 1
        for i in range(m):
            for j in range(n):
                if 0 <= i - 1 < m and 0 <= j - 1 < n and obstacleGrid[i][j] != 1:
                    if obstacleGrid[i - 1][j] == 0 and obstacleGrid[i][j - 1] == 0:
                        res[i][j] = res[i - 1][j] + res[i][j - 1]
                    if obstacleGrid[i - 1][j] != 0 and obstacleGrid[i][j - 1] == 0:
                        res[i][j] = res[i][j - 1]
                    if obstacleGrid[i - 1][j] == 0 and obstacleGrid[i][j - 1] != 0:
                        res[i][j] = res[i - 1][j]
                    if obstacleGrid[i - 1][j] != 0 and obstacleGrid[i][j - 1] != 0:
                        res[i][j] = 0
        return res[-1][-1]


if __name__ == "__main__":
    mat = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    mat = [[0]]
    # mat = [[0, 1]]
    # mat = [[1, 0]]
    print(Solution().uniquePathsWithObstacles(mat))
