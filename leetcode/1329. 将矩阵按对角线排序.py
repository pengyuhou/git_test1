class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        res = [[0 for _ in range(n)] for _ in range(m)]




        for y in range(n):
            ret = []
            tmp = y
            x = 0
            while True:
                if 0 <= x < m and 0 <= y < n:
                    ret.append(mat[x][y])
                    x += 1
                    y += 1
                else:
                    break
            ret.sort()
            x = 0
            y = tmp
            for i in range(len(ret)):
                res[x][y] = ret[i]
                x += 1
                y += 1

        for x in range(m):
            ret = []
            tmp = x
            y = 0
            while True:
                if 0 <= x < m and 0 <= y < n:
                    ret.append(mat[x][y])
                    x += 1
                    y += 1
                else:
                    break
            ret.sort()
            x = tmp
            y = 0
            for i in range(len(ret)):
                res[x][y] = ret[i]
                x += 1
                y += 1
        return res


if __name__ == "__main__":
    mat = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]
    print(Solution().diagonalSort(mat))
