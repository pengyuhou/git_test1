class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        mat = matrix
        m=len(mat)
        n=len(mat[0])
        ret=[]
        for i in range(m):
            res=[]
            for j in range(n):
                res.append(None)
            ret.append(res)
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    ret[i][j] = 0
                    for t in range(n):
                        if mat[i][t] != 0:
                            ret[i][t] = 0
                    for r in range(m):
                        if mat[r][j] != 0:
                            ret[r][j]=0
        for i in range(m):
            for j in range(n):
                if ret[i][j] is None:
                    ret[i][j] = mat[i][j]
        matrix[:]=ret


if __name__ == "__main__":
    mat=[
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    print(Solution().setZeroes(matrix = mat))



