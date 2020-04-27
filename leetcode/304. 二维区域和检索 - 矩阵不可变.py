class NumMatrix(object):
    def __init__(self, matrix):

        if matrix==[] or matrix==[[]] or matrix==[[[]]]:
            pass
        else:

            self.m =matrix
            m, n = len(matrix), len(matrix[0])
            self.dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
            self.dp[1][1] = matrix[0][0]
            for i in range(1, n + 1):
                self.dp[1][i] = self.dp[1][i - 1] + matrix[0][i - 1]
            for i in range(1, m + 1):
                self.dp[i][1] = self.dp[i - 1][1] + matrix[i - 1][0]
            for i in range(2, m + 1):
                for j in range(2, n + 1):
                    self.dp[i][j] = self.dp[i - 1][j] + self.dp[i][j - 1] - self.dp[i - 1][j - 1] + matrix[i - 1][j - 1]



    def sumRegion(self, row1, col1, row2, col2):
        return self.dp[row2+1][col2+1] - self.dp[row2+1][col1] - self.dp[row1][col2+1] + self.dp[row1][col1]


# Your NumMatrix object will be instantiated and called as such:



# class NumMatrix:
#
#     def __init__(self, matrix):
#         if not matrix or not matrix[0]:pass
#         else:
#             row = len(matrix)
#             col = len(matrix[0])
#             self.dp = [[ 0 ] * (col + 1) for _ in range(row + 1)]
#             # 求行的前缀和
#             for i in range(1, row + 1):
#                 for j in range(1 ,col + 1):
#                     self.dp[i][j] = self.dp[i][j - 1] + matrix[i - 1][j - 1]
#             # 求列的前缀和
#             for j in range(1, col + 1):
#                 for i in range(1, row + 1):
#                     self.dp[i][j] += self.dp[i - 1][j]
#         print(self.dp)
#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         return self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - self.dp[row2 + 1][col1] + self.dp[row1][col1]

matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]
# matrix= [[[[[]]]]]
obj = NumMatrix(matrix)
param_1 = obj.sumRegion(2, 1, 4, 3)
print(param_1)