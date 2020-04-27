class Solution(object):
    count = 0

    def c_num(self, A):
        count = 0
        for i in A:
            count += i.count(0)
        return count

    def uniquePathsIII(self, grid):
        m = len(grid)
        n = len(grid[0])
        pd = grid.copy()
        mat = grid.copy()

        def dfs(mat, pd, x, y):
            if self.c_num(pd) == 0 and mat[x][y] == 2:
                self.count += 1
                return
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                xi = x + dx
                yi = y + dy
                if 0 <= xi < m and 0 <= yi < n:
                    if mat[xi][yi] == -1 or (mat[xi][yi] == 0 and pd[xi][yi] == -2):
                        continue
                    if mat[xi][yi] == 0 and pd[xi][yi] != -2:
                        pd[xi][yi] = -2
                        dfs(mat, pd, xi, yi)
                        pd[xi][yi] = 0
                    if mat[xi][yi] == 2 and self.c_num(pd) == 0:
                        dfs(mat, pd, xi, yi)
                        return

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    dfs(mat, pd, i, j)
                    return self.count


if __name__ == '__main__':
    print(Solution().uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]))
