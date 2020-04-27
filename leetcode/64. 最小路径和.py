class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        cp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            if i == 0:
                cp[i][0] = grid[i][0]
            else:
                cp[i][0] = cp[i - 1][0] + grid[i][0]
        for i in range(n):
            if i == 0:
                cp[0][i] = grid[0][i]
            else:
                cp[0][i] = cp[0][i - 1] + grid[0][i]
        for i in range(1, m):
            for j in range(1, n):
                cp[i][j] = min(cp[i - 1][j], cp[i][j - 1]) + grid[i][j]
        return cp[-1][-1]

if __name__ == "__main__":
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    print(Solution().minPathSum(grid))
