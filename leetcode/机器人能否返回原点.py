class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x, y = 0, 0
        for i in moves:
            if i == 'U':
                y += 1
            if i == 'D':
                y -= 1
            if i == 'L':
                x -= 1
            if i == 'R':
                x += 1
        if x == 0 and y == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    moves='UDD'
    S=Solution()
    print(S.judgeCircle(moves))



