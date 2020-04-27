class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        ret=[]
        for i in range(m):
            for j in range(n):
                ret.append(matrix[i][j])
        ret.sort()
        return target in ret


if __name__ == '__main__':

    mat = [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]
    mat=[]
    target = 20
    print(Solution().findNumberIn2DArray(mat,target))







