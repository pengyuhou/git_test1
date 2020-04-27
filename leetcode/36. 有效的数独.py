class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    key = board[i][j]
                    for m in range(9):
                        if m == j:
                            continue
                        else:
                            if board[i][m] == key:
                                return False
                    for m in range(9):
                        if m == i:
                            continue
                        else:
                            if board[m][j] == key:
                                return False
                    a1 = i // 3
                    b1 = j // 3
                    for t in range(a1, (a1 + 1) * 3):
                        for h in range(b1, (b1 + 1) * 3):
                            if key == board[t][h] and (i!=t or j!=h):
                                return False
        return True


if __name__ == "__main__":
    nums = [[".", ".", ".", ".", "5", ".", ".", "1", "."], [".", "4", ".", "3", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "3", ".", ".", "1"], ["8", ".", ".", ".", ".", ".", ".", "2", "."],
            [".", ".", "2", ".", "7", ".", ".", ".", "."], [".", "1", "5", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "2", ".", ".", "."], [".", "2", ".", "9", ".", ".", ".", ".", "."],
            [".", ".", "4", ".", ".", ".", ".", ".", "."]]
    print(Solution().isValidSudoku(nums))
