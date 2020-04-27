class Solution(object):
    def countBattleships(self, board):
        count = 0
        m = len(board)
        n = len(board[0])
        for x in range(m):
            for y in range(n):
                if board[x][y]=='X':
                    res = [[x,y]]
                    while True:
                        l = len(res)
                        board[x][y] = '.'
                        for xi,yi in res:
                            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                                x_cur = xi + dx
                                y_cur = yi + dy
                                if 0 <= x_cur < m and 0 <= y_cur < n:
                                    if board[x_cur][y_cur] == 'X':
                                        board[x_cur][y_cur] = '.'
                                        res.append([x_cur,y_cur])
                        if len(res)-l == 0:
                            break
                    count += 1
        return count






if __name__ == "__main__":
    board = [['X','.','.','X'],
            ['.','.','.',''],
            ['X','X','X','X']]
    print(Solution().countBattleships(board))

