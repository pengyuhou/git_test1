class Solution(object):
    def spiralOrder(self, matrix):
        if matrix==[]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        x = 0
        y = 0
        dx = 0
        dy = 1
        ans = []
        for _ in range(m*n):
            ans.append(matrix[x][y])
            matrix[x][y] = None
            if 0<=(x+dx)<m and 0<=(y+dy)<n:
                if matrix[x+dx][y+dy] == None:
                    dx,dy=dy,-dx
                x += dx
                y += dy
            else:
                dx, dy = dy, -dx
                x += dx
                y += dy
        return ans

if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(Solution().spiralOrder(matrix))