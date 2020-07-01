# class Solution:
#     def solve(self, board):
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         if not board:
#             return
#         m, n = len(board), len(board[0])
#
#         def isedge(x_pos, y_pos):
#             if x_pos == 0 or x_pos == m - 1 or y_pos == 0 or y_pos == n - 1:
#                 return True
#             else:
#                 return False
#
#
#         for i in range(m):
#             for j in range(n):
#                 ret = []
#                 if board[i][j] == 'O' and not isedge(i, j):
#                     mark = [[False for _ in range(n)] for _ in range(m)]
#                     ret.append([i, j])
#                     queue = [[i, j]]
#                     mark[i][j] = True
#                     flag = False
#                     while queue:
#                         for _ in range(len(queue)):
#                             x, y = queue.pop(0)
#                             for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#                                 xi = x + dx
#                                 yi = y + dy
#                                 if board[xi][yi] == 'O' and not isedge(xi, yi) and not mark[xi][yi]:
#                                     ret.append([xi, yi])
#                                     queue.append([xi, yi])
#                                     mark[xi][yi] = True
#                                 if board[xi][yi] == 'O' and isedge(xi, yi):
#                                     flag = True
#                             if flag:
#                                 break
#                     if not flag:
#                         for x, y in ret:
#                             board[x][y] = 'X'

class Solution:
    def solve(self, board):
        if not board:
            return
        m, n = len(board), len(board[0])

        def dfs(x, y, pd, res):
            # if board[x][y] == 'X':
            #     return False
            if board[x][y] == 'O' and (x == 0 or x == m - 1 or y == 0 or y == n - 1):
                return False
            r = []
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                xi = x + dx
                yi = y + dy
                if board[xi][yi] == 'O' and not pd[xi][yi]:
                    pd[xi][yi] = True
                    res.append([xi, yi])
                    s = dfs(xi, yi, pd, res)
                    r.append(s)

            return all(r)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not (i == 0 or i == m - 1 or j == 0 or j == n - 1):
                    mark = [[False for _ in range(n)] for _ in range(m)]
                    mark[i][j] = True
                    x = [[i, j]]
                    if dfs(i, j, mark, x):
                        print(dfs(i, j, mark, x))
                        for a, b in x.copy():
                            board[a][b] = 'X'
        # print(board)


# print(Solution().solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]))

print(all([]))
