class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        ret = []
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    ret.append([i, j])
        for i, j in ret:
            for x in range(n):
                matrix[i][x] = 0
            for y in range(m):
                matrix[y][j] = 0



if __name__ == "__main__":
    grid = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    print(Solution().setZeroes(grid))
