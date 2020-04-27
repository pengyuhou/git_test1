import copy
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        mark = copy.deepcopy(board)
        res = copy.deepcopy(board)
        m, n = len(board), len(board[0])
        for x in range(m):
            for y in range(n):
                count_live = 0
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]:
                    xi = x + dx
                    yi = y + dy
                    if 0 <= xi < m and 0 <= yi < n:
                        if mark[xi][yi]:
                            count_live += 1
                if res[x][y]:
                    if count_live < 2:
                        res[x][y] = 0
                    if count_live == 2 or count_live == 3:
                        continue
                    if count_live > 3:
                        res[x][y] = 0
                else:
                    if count_live == 3:
                        res[x][y] = 1
        board[:] = res



if __name__ == "__main__":
    grid = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]
    print(Solution().gameOfLife(grid))

