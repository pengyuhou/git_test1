class Solution(object):
    def rotate(self, matrix):
        m,n = len(matrix),len(matrix[0])

        cp = [[0 for _ in range(n)]for _ in range(m)]


        for i in range(m):
            for j in range(n):
                cp[i][j] = matrix[n-1-j][i]
        matrix[:] = cp












if __name__ == "__main__":
    matrix =[
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(Solution().rotate(matrix))













