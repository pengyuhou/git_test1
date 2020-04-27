class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        a = 0
        while c - a ** 2 >= 0:
            if str((c-a**2)**0.5).split('.')[-1] == '0':
                return True
            a += 1
        return False

if __name__ == "__main__":

    c=5
    print(Solution().judgeSquareSum(11))
