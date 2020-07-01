class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        cur = [0, 0]
        dx, dy = 0, 1
        m, n = len(matrix), len(matrix[0])
        ret = []
        mark = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m * n):
            mark[cur[0]][cur[1]] = True
            ret.append(matrix[cur[0]][cur[1]])
            if (cur[0] + dx < 0 or cur[0] + dx >= m or cur[1] + dy < 0 or cur[1] + dy >= n) or mark[cur[0] + dx][
                cur[1] + dy]:
                dx, dy = dy, -dx
            cur[0] += dx
            cur[1] += dy
        return ret

print(Solution().spiralOrder(matrix=[[]]))
