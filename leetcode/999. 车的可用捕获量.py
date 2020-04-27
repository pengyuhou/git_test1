class Solution(object):
    def numRookCaptures(self, board):
        m = 8
        n = 8
        located_rook = None
        located_bishop = []
        located_pawn = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'R':
                    located_rook = [i, j]
                if board[i][j] == 'B':
                    located_bishop.append([i, j])
                if board[i][j] == 'p':
                    located_pawn.append([i, j])
        a = None
        b = None
        for x_bishop, y_bishop in located_bishop:
            if located_rook[0] == x_bishop:
                if y_bishop < located_rook[1]:
                    if a is None:
                        a = y_bishop
                    else:
                        a = max(a, y_bishop)
                else:
                    if b is None:
                        b = y_bishop
                    else:
                        b = min(b, y_bishop)
        c = None
        d = None
        for x_bishop, y_bishop in located_bishop:
            if located_rook[1] == y_bishop:
                if x_bishop < located_rook[0]:
                    if c is None:
                        c = x_bishop
                    else:
                        c = max(c, x_bishop)
                else:
                    if d is None:
                        d = x_bishop
                    else:
                        d = min(d, x_bishop)
        kexingyu_1 = None
        kexingyu_3 = None
        kexingyu_2 = None
        kexingyu_4 = None
        if a is not None:
            kexingyu_1 = (range(a, located_rook[1]))
        if b is not None:
            kexingyu_2 = (range(located_rook[1] + 1, b))
        if c is not None:
            kexingyu_3 = (range(c, located_rook[0]))
        if d is not None:
            kexingyu_4 = (range(located_rook[0] + 1, d))
        count = 0
        flag1 = False
        flag2 = False
        flag3 = False
        flag4 = False
        for i, j in located_pawn:
            if i == located_rook[0] and j < located_rook[1] and not flag1:
                if kexingyu_1 is not None:
                    if j in kexingyu_1:
                        count += 1
                        flag1 = True
                        continue
                else:

                    count += 1
                    flag1 = True
                    continue

            if i == located_rook[0] and j > located_rook[1] and not flag2:
                if kexingyu_2 is not None:
                    if j in kexingyu_2:
                        count += 1
                        flag2 = True
                        continue
                else:

                    count += 1
                    flag2 = True
                    continue
            if j == located_rook[1] and i < located_rook[0] and not flag3:
                if kexingyu_3 is not None:
                    if i in kexingyu_3:
                        count += 1
                        flag3 = True
                        continue
                else:
                    count += 1
                    flag3 = True
                    continue
            if j == located_rook[1] and i > located_rook[0] and not flag4:

                if kexingyu_4 is not None:
                    if i in kexingyu_4:
                        count += 1
                        flag4 = True
                        continue
                else:
                    count += 1
                    flag4 = True
                    continue
        return count

if __name__ == "__main__":
    board=[[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
    board = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
    board =[[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
    print(Solution().numRookCaptures(board))



























