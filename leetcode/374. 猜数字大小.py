# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left < right:
            mid = (left + right) // 2
            if not guess(left):
                return left
            if not guess(right):
                return right
            res = guess(mid)
            if res == 0:
                return mid
            elif res < 0:
                right = mid
            else:
                left = mid
