class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m , n = len(matrix),len(matrix[0])
        res = [[0 for _ in range(n)]for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = matrix[n-j-1][i]
        matrix[:] = res





if __name__ == "__main__":
    matrix =[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
    print(Solution().rotate(matrix))