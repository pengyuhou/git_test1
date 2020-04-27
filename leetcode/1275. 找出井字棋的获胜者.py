class Solution(object):
    def tictactoe(self, moves):
        a = [moves[i] for i in range(len(moves)) if i % 2 == 0]
        b = [moves[i] for i in range(len(moves)) if i % 2 != 0]
        if [0, 0] in a and [1, 1] in a and [2, 2] in a:
            return 'A'
        if [2, 0] in a and [1, 1] in a and [0, 2] in a:
            return 'A'
        if [0, 0] in a and [0, 1] in a and [0, 2] in a:
            return 'A'
        if [1, 0] in a and [1, 1] in a and [1, 2] in a:
            return 'A'
        if [2, 0] in a and [2, 1] in a and [2, 2] in a:
            return 'A'
        if [0, 0] in a and [1, 0] in a and [2, 0] in a:
            return 'A'
        if [0, 1] in a and [1, 1] in a and [2, 1] in a:
            return 'A'
        if [0, 2] in a and [1, 2] in a and [2, 2] in a:
            return 'A'
        if [0, 0] in b and [1, 1] in b and [2, 2] in b:
            return 'B'
        if [2, 0] in b and [1, 1] in b and [0, 2] in b:
            return 'B'
        if [0, 0] in b and [0, 1] in b and [0, 2] in b:
            return 'B'
        if [1, 0] in b and [1, 1] in b and [1, 2] in b:
            return 'B'
        if [2, 0] in a and [2, 1] in a and [2, 2] in a:
            return 'B'
        if [0, 0] in b and [1, 0] in b and [2, 0] in b:
            return 'B'
        if [0, 1] in b and [1, 1] in b and [2, 1] in b:
            return 'B'
        if [0, 2] in b and [1, 2] in b and [2, 2] in b:
            return 'B'
        if len(moves)==9:
            return 'Draw'
        else:
            return 'Pending'


if __name__ == '__main__':
    moves = [[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]
    moves = [[0, 0], [1, 1]]
    moves = [[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]
    print(Solution().tictactoe(moves))







