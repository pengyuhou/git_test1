import math


class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        a = math.log(n)
        b = math.log(2)
        res = str(a / b)

        if res[-1] == str(0):
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfTwo(0))

    a = 'ada'
    b = 'jj'
    print(f'{a}哈哈{b}')
