class Solution(object):
    def shift(self,mat):
        m = len(mat)
        n = len(mat[0])
        res = []
        for i in range(m):
            a = []
            for j in range(n):
                a.append(None)
            res.append(a)
        for i in range(m):
            for j in range(n):
                if i != 0 and j == 0:
                    res[i][j] = mat[i-1][n-1]
                if j!= n-1:
                    res[i][j+1] = mat[i][j]
                if i == 0 and j == 0:
                    res[i][j] = mat[m-1][n-1]
        return res
    def shiftGrid(self, grid, k):
        for i in range(k):
            grid = self.shift(grid)
        return grid




if __name__ == "__main__":

    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 1
    print(Solution().shiftGrid(grid,6))














