class Solution(object):
    def surfaceArea(self, grid):
        n = len(grid)
        if n==1:
            return grid[0][0]*4+2
        count = 0
        x = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] != 0:
                    x += 1
                if i == 0 and j == 0:
                    count += 2 * grid[i][j]
                    if grid[i][j] > grid[i][j + 1]:
                        count += grid[i][j] - grid[i][j + 1]
                    if grid[i][j] > grid[i + 1][j]:
                        count += grid[i][j] - grid[i + 1][j]
                        continue
                elif i == 0 and j == n - 1:
                    count += 2 * grid[i][j]
                    if grid[i][j] > grid[i][j - 1]:
                        count += grid[i][j] - grid[i][j - 1]
                    if grid[i][j] > grid[i + 1][j]:
                        count += grid[i][j] - grid[i + 1][j]
                        continue
                elif i == n - 1 and j == 0:
                    count += 2 * grid[i][j]
                    if grid[i][j] > grid[i][j + 1]:
                        count += grid[i][j] - grid[i][j + 1]
                    if grid[i][j] > grid[i - 1][j]:
                        count += grid[i][j] - grid[i - 1][j]
                        continue
                elif i == n - 1 and j == n - 1:
                    count += 2 * grid[i][j]
                    if grid[i][j] > grid[i][j - 1]:
                        count += grid[i][j] - grid[i][j - 1]
                    if grid[i][j] > grid[i - 1][j]:
                        count += grid[i][j] - grid[i - 1][j]
                        continue
                elif i == 0 and j != 0 and j != n - 1:
                    count += grid[i][j]
                    if grid[i][j] > grid[i][j - 1]:
                        count += grid[i][j] - grid[i][j - 1]
                    if grid[i][j] > grid[i][j + 1]:
                        count += grid[i][j] - grid[i][j + 1]
                    if grid[i][j] > grid[i + 1][j]:
                        count += grid[i][j] - grid[i + 1][j]
                        continue
                elif j == 0 and i != 0 and i != n - 1:
                    count += grid[i][j]
                    if grid[i][j] > grid[i][j + 1]:
                        count += grid[i][j] - grid[i][j + 1]
                    if grid[i][j] > grid[i - 1][j]:
                        count += grid[i][j] - grid[i - 1][j]
                    if grid[i][j] > grid[i + 1][j]:
                        count += grid[i][j] - grid[i + 1][j]
                        continue
                elif i == n - 1 and j != 0 and j != n - 1:
                    count += grid[i][j]
                    if grid[i][j] > grid[i][j - 1]:
                        count += grid[i][j] - grid[i][j - 1]
                    if grid[i][j] > grid[i][j + 1]:
                        count += grid[i][j] - grid[i][j + 1]
                    if grid[i][j] > grid[i - 1][j]:
                        count += grid[i][j] - grid[i - 1][j]
                        continue
                elif j == n - 1 and i != 0 and i != n - 1:
                    count += grid[i][j]
                    if grid[i][j] > grid[i - 1][j]:
                        count += grid[i][j] - grid[i - 1][j]
                    if grid[i][j] > grid[i + 1][j]:
                        count += grid[i][j] - grid[i + 1][j]
                    if grid[i][j] > grid[i][j - 1]:
                        count += grid[i][j] - grid[i][j - 1]
                        continue
                else:
                    if grid[i][j] > grid[i][j + 1]:
                        count += grid[i][j] - grid[i][j + 1]
                    if grid[i][j] > grid[i][j - 1]:
                        count += grid[i][j] - grid[i][j - 1]
                    if grid[i][j] > grid[i - 1][j]:
                        count += grid[i][j] - grid[i - 1][j]
                    if grid[i][j] > grid[i + 1][j]:
                        count += grid[i][j] - grid[i + 1][j]
        count += 2 * x
        return count

if __name__ == "__main__":
    # grid=[[1,1,1],[1,0,1],[1,1,1]]
    grid=[[2,2,2],[2,1,2],[2,2,2]]

    print(Solution().surfaceArea(grid))

























