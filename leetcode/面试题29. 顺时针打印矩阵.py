"""
class Solution(object):
    def spiralOrder(self, matrix):
        r, i, j, di, dj = [], 0, 0, 0, 1
        if matrix != []:
            for _ in range(len(matrix) * len(matrix[0])):
                r.append(matrix[i][j])
                matrix[i][j] = None
                if matrix[(i + di) % len(matrix)][(j + dj) % len(matrix[0])] == None:
                    di, dj = dj, -di
                i += di
                j += dj
        return r
"""
class Solution(object):
    def spiralOrder(self, matrix):
        if matrix==[]:
            return []
        res = []
        x = 0
        y = 0
        dx = 0
        dy =1
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m*n):
            res.append(matrix[x][y])
            matrix[x][y] = None
            xi = x + dx
            yi = y + dy
            if matrix[xi%m][yi%n]==None:
                dx,dy = dy,-dx
                x += dx
                y += dy
                continue
            x = xi
            y = yi
        return res




if __name__ == "__main__":
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(Solution().spiralOrder(matrix))